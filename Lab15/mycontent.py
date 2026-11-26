import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

MODEL = "openrouter/free"

MENU = {
    "Latte": 5.25,
    "Americano": 4.00,
    "Cold brew": 5.00,
    "Mocha": 5.75,
    "Chai latte": 5.50,
    "Blueberry muffin": 3.50,
}

INFO = {
    "Hours": "Monday-Saturday, 7:00 AM-10:00 PM; Sunday closed",
    "Location": "Campus Center, 1234 University Avenue, Honolulu, HI",
    "Wi-Fi password": "manoa-study",
    "Sizes": "Regular is the listed price; Large adds $1.00",
    "Iced drinks": "Any drink can be made iced at no extra charge",
}

TEST_QUESTIONS = [
    "How much is a latte?",
    "Are you open Sunday?",
    "Do you sell sushi?",
    "Who won the Super Bowl?",
]


def build_system_prompt(menu: dict[str, float], info: dict[str, str]) -> str:
    prompt = (
        "You are a cheerful barista at Mānoa Bytes Café. "
        "Answer only using the café information below. "
        "You may take orders and add up totals using these prices. "
        "If the information does not answer the question, reply exactly: "
        "\"I'm not sure, please ask at the counter.\"\n\n"
        "Menu:\n"
    )

    for item, price in menu.items():
        prompt += f"- {item}: ${price:.2f}\n"

    prompt += "\nCafé information:\n"
    for label, value in info.items():
        prompt += f"- {label}: {value}\n"

    return prompt


def main() -> None:
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.environ["OPENROUTER_API_KEY"],
    )
    system_prompt = build_system_prompt(MENU, INFO)

    for question in TEST_QUESTIONS:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": question},
            ],
        )
        print(f"Q: {question}")
        print(f"A: {response.choices[0].message.content}\n")


if __name__ == "__main__":
    main()