🧠 FoodieSpot AI Reservation Agent
FoodieSpot_Reservation_Agent is a conversational AI assistant that helps users book restaurant reservations or get dining recommendations — just like a human receptionist. Built using Groq + LLaMA 3, it uses a lightweight, custom tool-calling framework (no LangChain) and a sleek Streamlit frontend for chat-style interaction.

🚀 Features
🗣️ Multi-turn conversation with context memory

🍽️ Understands cuisine or specific restaurant names

📍 Extracts location, party size, and reservation time

🤖 Automatically follows up for missing details

🔧 Custom tool-calling implementation (no LangChain)

🧠 Powered by llama3-70b-8192 via Groq API

💻 Deployed with a user-friendly Streamlit chatbot UI

📁 Project Structure
foodiespot-reservation-agent/
├── app/
│ └── main.py → Streamlit frontend
├── agent/
│ ├── agent.py → Core conversation logic
│ ├── intent_handler.py → Routes intent to appropriate tool
│ └── prompts.py → System prompt & few-shot examples
├── tools/
│ ├── reservation_tools.py → Handles reservation logic
│ ├── recommendation_tools.py → Suggests restaurant options
│ └── utils.py → Helper functions
├── data/
│ └── restaurants.py → Static dataset of 40 restaurants
├── .env.example → Template for environment config
├── requirements.txt → Project dependencies
└── README.md

⚙️ Setup Instructions
Create and activate a virtual environment:

On Windows:
python -m venv venv
venv\Scripts\activate

On Mac/Linux:
python3 -m venv venv
source venv/bin/activate

Install dependencies:
pip install -r requirements.txt

Add your Groq API key:
Copy .env.example to .env
Add GROQ_API_KEY=your_groq_api_key_here

▶️ Run the App
streamlit run app/main.py

Then open the URL shown (usually http://localhost:8501) in your browser.

💬 Example Conversation
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
