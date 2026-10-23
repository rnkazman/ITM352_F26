# Save the dictionary of quiz questions to a JSON file
import json

questions = {
    "What is the capital of France?": ["Paris", "Toulouse", "Nice", "Avignon"],
    "What is the capital of Germany?": ["Berlin", "Munich", "Hamburg", "Frankfurt"],
    "What is the airspeed of an unladen swallow?": ["10", "12", "8", "15"],
    "The Last Supper was painted by which artist?": ["da Vinci", "Michelangelo", "Raphael", "Caravaggio"],
    "Which NHL player has the most career points?": ["Wayne Gretzky", "Mario Lemieux", "Jaromir Jagr", "Sidney Crosby"],
    "Which classic novel opens with the line 'Call me Ishmael'?": ["Moby Dick", "The Great Gatsby", "The Old Man and the Sea", "The Scarelet Letter"],
    "What is the largest planet in our solar system?": ["Jupiter", "Saturn", "Uranus", "Neptune"]
}

filename = "quiz_questions.json"

# Open the file in write mode and save the dictionary as JSON
with open(filename, 'w') as file:
    json.dump(questions, file, indent=2)

print(f"Quiz questions saved to {filename}")
