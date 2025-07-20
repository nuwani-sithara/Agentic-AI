import streamlit as st
from agent import get_support_reply

# ---------------------------
# Page Setup
# ---------------------------
st.set_page_config(page_title="Mental Wellness Assistant", layout="centered")

# ---------------------------
# CSS Styling + Animated BG
# ---------------------------
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600&display=swap');

        html, body, [class*="css"] {
            font-family: 'Quicksand', sans-serif;
            background: linear-gradient(-45deg, #fceff9, #e0f7fa, #f0f4c3, #ffe0b2);
            background-size: 400% 400%;
            animation: gradientBG 20s ease infinite;
            color: #333;
        }
            
        html, body, [class*="css"] {
            border: 5px dashed red;
            animation: gradientBG 10s ease infinite;
        }
        .stTextInput > div > div > input {
            border-radius: 10px;
            padding: 12px;
            border: 1px solid #ccc;
        }

        @keyframes gradientBG {
            0% {background-position: 0% 50%;}
            50% {background-position: 100% 50%;}
            100% {background-position: 0% 50%;}
        }

        .stTextInput > div > div > input {
            border-radius: 10px;
            padding: 12px;
            border: 1px solid #ccc;
        }

        .big-title {
            font-size: 2.5rem;
            text-align: center;
            color: #DA70D6;
            font-weight: 600;
            margin-bottom: 10px;
        }

        .subtitle {
            text-align: center;
            font-size: 1.1rem;
            color: #555;
        }

        .reply-box {
            background-color: #FFF;
            padding: 16px;
            border-radius: 15px;
            border: 2px solid #FFB6C1;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# ---------------------------
# UI
# ---------------------------

# Cute banner image
# st.image("assets/cute_banner.png", use_container_width=True)

st.markdown('<div class="big-title">🌼 Mental Wellness Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">I’m here to support you. Choose the vibe that suits you best 🌈</div>', unsafe_allow_html=True)

# Support mode selection
mode = st.selectbox(
    "🌟 Select your support mode:",
    (
        "Mental Support 🧠",
        "Motivation 💪",
        "Study Buddy 📚",
        "Work Stress Relief 💼",
        "Daily Affirmations 🌞"
    )
)

mode_map = {
    "Mental Support 🧠": "mental_support",
    "Motivation 💪": "motivation",
    "Study Buddy 📚": "study_buddy",
    "Work Stress Relief 💼": "work_stress",
    "Daily Affirmations 🌞": "affirmations"
}

# Background Music
with st.expander("🎶 Background Music"):
    music_enabled = st.checkbox("Play soft background music 🎧")
    if music_enabled:
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3")

# Chat input & history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("💬 What's on your mind today?")

if user_input:
    reply = get_support_reply(user_input, mode=mode_map[mode])
    st.session_state.chat_history.append((user_input, reply))
    st.markdown(f'<div class="reply-box">🧸 <strong>Agent:</strong><br>{reply}</div>', unsafe_allow_html=True)

if st.session_state.chat_history:
    with st.expander("📝 View Chat History"):
        for u, r in st.session_state.chat_history:
            st.markdown(f"**You:** {u}")
            st.markdown(f"**Agent:** {r}")
