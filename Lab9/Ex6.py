# Read a file of quiz questions and save as a dictionary.
import json

filename = "quiz_questions.json"
with open(filename, 'r') as file:
    questions = json.load(file)

print(questions)
