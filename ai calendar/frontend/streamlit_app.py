import streamlit as st
import requests

API_URL = "https://your-api-url/chat"

st.set_page_config(page_title="AI Appointment Scheduler")
st.title("📆 Book an Appointment")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Ask me to book an appointment...")

if user_input:
    st.session_state.chat_history.append(("user", user_input))
    with st.spinner("Thinking..."):
        res = requests.post(API_URL, json={"message": user_input}).json()
        st.session_state.chat_history.append(("agent", res["response"]))

for speaker, message in st.session_state.chat_history:
    st.chat_message(speaker).write(message)
