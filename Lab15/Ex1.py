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

response = client.chat.completions.create(
    model=MODEL,
    messages=[{"role": "user", "content": "Suggest a name for a shave ice shop in Honolulu."}]
)
print(response.choices[0].message.content)