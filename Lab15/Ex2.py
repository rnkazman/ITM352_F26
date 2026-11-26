import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(Path(__file__).resolve().parent / ".env")
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"]
)
MODEL = "openrouter/free"

my_messages = [
    {"role": "system", "content": "You are a pirate-themed assistant for Aloha Bikes, a bike rental shop in Waikiki. Answer in 10 words or less."},
    {"role": "user", "content": "What should I bring on a bike ride to Diamond Head?"}
]

response = client.chat.completions.create(
    model=MODEL,
    messages=my_messages
)
print(response.choices[0].message.content)