



import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from agent.agent import handle_user_input
from tools.utils import format_datetime
from data.restaurants import get_restaurants

# Set page config
st.set_page_config(page_title="FoodieSpot Chat", page_icon="🍽️", layout="centered")

# Title and subtitle
st.title("🍽️ FoodieSpot Reservation Agent")
st.markdown("**Chat with our AI assistant to reserve a table or get dining recommendations!**")

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi there! How can I help you today? 😊"}
    ]

# Display message history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    else:
        st.chat_message("assistant").markdown(msg["content"])

# Chat input box
user_prompt = st.chat_input("Type your message here...")

# Generate a unique or fixed session ID for the conversation
session_id = "default"  # You can make this dynamic using user login/IP if needed

# On user input
if user_prompt:
    # Show user message
    st.chat_message("user").markdown(user_prompt)
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    # Generate response with session tracking
    response = handle_user_input(user_prompt, session_id=session_id)

    # Show assistant message
    st.chat_message("assistant").markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
