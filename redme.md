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

## 📁 Project Structure

foodiespot-reservation-agent/
├── app/
│ └── main.py # Streamlit frontend
├── agent/
│ ├── agent.py # Core conversation logic
│ ├── intent_handler.py # Routes intent to appropriate tool
│ └── prompts.py # System prompt & few-shot examples
├── tools/
│ ├── reservation_tools.py # Makes reservations from params
│ ├── recommendation_tools.py # Suggests restaurant options
│ └── utils.py # Helper functions
├── data/
│ └── restaurants.py # Static dataset of 40 restaurants
├── .env.example # Template for environment config
├── requirements.txt # Project dependencies
└── README.md 


Create and activate a virtual environment

python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

Install dependencies

pip install -r requirements.txt

Run this project
streamlit run app/main.py


Example Conversation

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