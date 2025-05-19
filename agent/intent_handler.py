

import json
from tools.reservation_tools import make_reservation
from tools.recommendation_tools import get_recommendation

def route_intent(parsed_response, original_input):
    try:
        parsed = json.loads(parsed_response)
        intent = parsed.get("intent")
        params = parsed.get("params", {})

        if intent == "make_reservation":
            restaurant_name = params.get("restaurant_name", "the selected restaurant")
            num_people = params.get("num_people") or params.get("party_size", "some people")
            time = params.get("time", "an available time")
            cuisine = params.get("cuisine", "your preferred cuisine")
            location = params.get("location", "your preferred location")

            make_reservation(**params)  # Optionally log or trigger a real reservation

            return (
                f"✅ Reservation confirmed for {num_people} people at **{restaurant_name}** "
                f"({cuisine}) in **{location}** at **{time}**. Enjoy your meal! 🍽️"
            )

        elif intent == "get_recommendation":
            # ✅ Only pass supported arguments
            allowed_keys = ["location", "diet"]
            clean_params = {k: v for k, v in params.items() if k in allowed_keys}

            cuisine = params.get("cuisine", "any cuisine")
            location = params.get("location", "your location")

            recommended = get_recommendation(**clean_params)
            if recommended:
                return (
                    f"🍴 Based on your preference for **{cuisine}** in **{location}**, "
                    f"I recommend **{recommended}**!"
                )
            else:
                return "🙁 Sorry, I couldn't find any suitable restaurants right now."

        else:
            return "❓ Sorry, I didn't understand your request. Could you rephrase it?"

    except json.JSONDecodeError:
        return "⚠️ I couldn't understand the response format. Please try again."
    except Exception as e:
        return f"⚠️ Unexpected error: {str(e)}"
