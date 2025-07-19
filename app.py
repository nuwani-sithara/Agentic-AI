# app.py

import streamlit as st
from agent import get_support_reply

st.set_page_config(page_title="Mental Wellness Assistant", layout="centered")

st.title("🧘‍♀️ Mental Wellness Assistant")
st.markdown("Hello! I'm here to support you. Tell me how you're feeling today 💬")

user_input = st.text_input("What's on your mind?")

if user_input:
    reply = get_support_reply(user_input)
    st.markdown(f"**Agent:** {reply}")
