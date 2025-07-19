# agent.py

import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_support_reply(user_input):
    response = client.chat.completions.create(
        model="llama3-70b-8192",  # ✅ Updated model
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a kind and empathetic mental health support assistant. "
                    "Your job is to comfort users who are feeling mentally down, anxious, or stressed. "
                    "Offer kind words, emotional support, and gentle encouragement. Do not give medical advice."
                )
            },
            {"role": "user", "content": user_input}
        ]
    )
    return response.choices[0].message.content
