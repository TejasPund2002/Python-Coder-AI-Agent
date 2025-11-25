import streamlit as st
from google import genai

# Initialize client
client = genai.Client(api_key="AIzaSyDlirZJiQuJDSIpgxT2IWbUvaa7U3t2-sM")

SYSTEM_PROMPT = "You are a Python coding assistant. Reply ONLY with Python code."

# Streamlit UI
st.set_page_config(page_title="Python Coding Agent", layout="wide")
st.title("🐍 Python Coding Agent – Powered by Gemini 2.0")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "text": SYSTEM_PROMPT}
    ]

user_input = st.chat_input("Ask anything about Python...")

if user_input:
    st.session_state.messages.append({"role": "user", "text": user_input})
    st.chat_message("user").markdown(user_input)

    history = [
        {"role": msg["role"], "text": msg["text"]}
        for msg in st.session_state.messages
    ]

    # AI response
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=history
    )

    ai_text = response.text

    st.session_state.messages.append({"role": "assistant", "text": ai_text})

    st.chat_message("assistant").markdown(f"```python\n{ai_text}\n```")

else:
    for msg in st.session_state.messages:
        if msg["role"] != "system":
            st.chat_message(msg["role"]).markdown(msg["text"])
