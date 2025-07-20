# agent.py

import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_support_reply(user_input, mode="mental_support"):
    role_messages = {
        "mental_support": (
            "You are a kind and empathetic mental health support assistant. "
            "Your job is to comfort users who are feeling mentally down, anxious, or stressed. "
            "Offer kind words, emotional support, and gentle encouragement. Do not give medical advice."
        ),
        "motivation": (
            "You are a motivational coach. Give energetic and inspiring messages to boost someone's day. "
            "Provide short pep talks and encourage self-belief."
        ),
        "study_buddy": (
            "You are a supportive study companion. Encourage students, offer gentle reminders to stay focused, "
            "and praise them for their efforts."
        ),
        "work_stress": (
            "You are a calm mentor helping people deal with work-related stress. Offer gentle advice on relaxation, "
            "setting boundaries, and staying balanced."
        ),
        "affirmations": (
            "You are a daily affirmation bot. Provide short, uplifting affirmations that users can repeat to feel better."
        ),
    }

    system_message = role_messages.get(mode, role_messages["mental_support"])

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content

