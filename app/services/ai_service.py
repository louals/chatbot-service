import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_ai(message: str) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful quiz assistant."},
            {"role": "user", "content": message}
        ],
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()
