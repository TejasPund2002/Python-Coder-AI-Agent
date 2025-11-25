import streamlit as st
from google.genai import Client


API_KEY = st.secrets["GOOGLE_API_KEY"]

client = genai.Client(api_key=API_KEY)

st.title("My AI Agent")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("Ask something...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    response = client.responses.generate(
        model="gemini-2.0-flash",
        input=user_input
    )
    ai_msg = response.output_text
    st.session_state.messages.append({"role": "assistant", "content": ai_msg})

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

