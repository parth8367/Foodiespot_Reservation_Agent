# 🧠 FoodieSpot AI Reservation Agent

A conversational AI assistant that helps users book restaurant reservations or get dining recommendations — just like a human receptionist. Built using **Groq + LLaMA 3**, with a custom lightweight tool-calling framework (no LangChain), and a clean **Streamlit** frontend for chat-style interaction.

---

## 🚀 Features

- 🗣️ Multi-turn conversation with memory
- 🍽️ Understands cuisine or restaurant name
- 📍 Detects location, party size, and reservation time
- 🤖 Follows up for missing information automatically
- 🔧 Dynamic tool-calling without LangChain
- 🧠 Powered by `llama3-70b-8192` via Groq API
- 💻 Deployed through Streamlit with user-friendly chat UI

---

```
foodiespot-reservation-agent
├── app/
│   └── main.py                  # Streamlit frontend
├── agent/
│   ├── agent.py                 # Conversation flow and state
│   ├── intent_handler.py        # Routes parsed intent to tools
│   └── prompts.py               # Prompt + few-shot examples
├── tools/
│   ├── reservation_tools.py     # Reservation logic
│   ├── recommendation_tools.py  # Recommendation logic
│   └── utils.py                 # Utility functions
├── data/
│   └── restaurants.py           # Static list of restaurants
├── .env.example                 # API key template
├── requirements.txt             # Dependencies
└── README.md                    # Project documentation
```


## Create and activate a virtual environment

```
python -m venv venv
source venv/bin/activate
```

## Install dependencies
```
pip install -r requirements.txt
```

## changes in .env file
Grok_API = "XXXXXXXXXXXX"     write your own API

## Run this project
```
streamlit run app/main.py
```

## Example Conversation

👤: I want to book a restaurant

🤖: Is there a specific restaurant you'd like to book?

👤: South Indian

🤖: Which area or location do you prefer?

👤: Andheri

🤖: Is there a specific restaurant name?

👤: SamBar Pub 

🤖: For how many people should I book the table?

👤: 2

🤖: What time would you like the reservation?

👤: 8 PM

✅ Reservation confirmed for 2 people at SamBar Pub (South Indian) in Andheri at 8 PM!
