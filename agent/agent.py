
import os
import json
import re
import ast
from dotenv import load_dotenv
from groq import Groq
from agent.prompts import SYSTEM_PROMPT, FEW_SHOT_EXAMPLES
from agent.intent_handler import route_intent

# Load environment variables
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("❌ GROQ_API_KEY not found.")

# Initialize Groq client
client = Groq(api_key=api_key)

# In-memory session state
conversation_state = {}

def handle_user_input(user_input, session_id="default"):
    try:
        # Initialize session
        if session_id not in conversation_state:
            conversation_state[session_id] = {
                "intent": None,
                "params": {}
            }

        state = conversation_state[session_id]

        # Create prompt with context
        messages = [{"role": "system", "content": SYSTEM_PROMPT}] + FEW_SHOT_EXAMPLES
        intent_hint = f"Intent: {state['intent'] or 'unknown'}"
        context_prompt = f"{intent_hint}\nKnown info: {state['params']}\nUser said: {user_input}"
        messages.append({"role": "user", "content": context_prompt})

        # Call Groq LLM
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=messages,
            temperature=0.8
        )

        assistant_message = response.choices[0].message.content.strip()

        # ✅ Extract first valid JSON block using bracket counting
        bracket_stack = []
        json_start = None
        for i, char in enumerate(assistant_message):
            if char == '{':
                if json_start is None:
                    json_start = i
                bracket_stack.append(char)
            elif char == '}':
                if bracket_stack:
                    bracket_stack.pop()
                    if not bracket_stack:
                        json_end = i + 1
                        break
        else:
            return f"⚠️ Couldn't parse valid JSON block: `{assistant_message}`"

        cleaned = assistant_message[json_start:json_end]

        # ✅ Try parsing the cleaned JSON block
        try:
            parsed = json.loads(cleaned)
        except Exception:
            try:
                parsed = ast.literal_eval(cleaned)
            except Exception:
                return f"⚠️ Still couldn't parse assistant response: `{cleaned}`"

        parsed_intent = parsed.get("intent")
        params = parsed.get("params", {})

        # Lock the intent if not already set
        if not state["intent"]:
            state["intent"] = parsed_intent

        state["params"].update(params)

        # Ask for any missing parameters
        missing = check_missing_params(state["intent"], state["params"])
        if missing:
            return "🤖 " + " ".join(missing)

        # Route intent and reset session
        result = route_intent(json.dumps({
            "intent": state["intent"],
            "params": state["params"]
        }), user_input)

        conversation_state[session_id] = {"intent": None, "params": {}}
        return result

    except Exception as e:
        return f"❌ Error: {str(e)}"

def check_missing_params(intent, params):
    prompts = {
        "cuisine": "What type of cuisine or restaurant do you prefer?",
        "restaurant_name": "Is there a specific restaurant you'd like to book?",
        "location": "Which area or location do you prefer?",
        "party_size": "For how many people should I book the table?",
        "time": "What time would you like the reservation?"
    }

    required = {
        "make_reservation": ["party_size", "time", "location"],
        "get_recommendation": ["location"]
    }

    # Either restaurant_name or cuisine is acceptable
    if intent == "make_reservation" and not (params.get("restaurant_name") or params.get("cuisine")):
        return [prompts["restaurant_name"]]

    return [prompts[p] for p in required.get(intent, []) if not params.get(p)]
