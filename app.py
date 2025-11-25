import streamlit as st
from google import genai
from google.genai import Client


API_KEY = st.secrets["GOOGLE_API_KEY"]

client = Client(api_key=API_KEY)

st.title("Python 🐍 AI Agent")

# Session for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# User input
user_input = st.chat_input("Ask something...")
system_prompt = "You are a Python coding assistant. Reply with Python code only.any Other Language not allow"

def ask_agent(message):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=message, 
        config={
            "system_instruction": system_prompt
        }
    )
    return response.text


if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Generate AI res
    ai_msg=ask_agent(user_input)

    st.session_state.messages.append({"role": "assistant", "content": ai_msg})

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])





