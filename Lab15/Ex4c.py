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

system_context = input("Enter system context (or leave blank for default): ")

if not system_context.strip():
    system_context = "You are a helpful assistant for Aloha Bikes."
messages = [{"role": "system", "content": system_context}]
print("Welcome to your custom chatbot. Type 'exit', 'quit', or 'bye' to end the conversation.")

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "bye"]:
        break
    if not user_input.strip():
        print("Please enter a message.")
        continue
    messages.append({"role": "user", "content": user_input})
    
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages
    )
    
    reply = response.choices[0].message.content
    print(f"Assistant: {reply}")
    
    messages.append({"role": "assistant", "content": reply})
    print(len(messages))