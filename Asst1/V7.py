# Interactive quiz system, sixth version
# Make a dictionary with the questions and correct answers
# Allow the user to choose the option by its label
# Improve the look and usability. Keep track of correct answers.
# Randomize the order of the questions and the order of the answers for each question.
# Refactor the code to use functions.

from string import ascii_lowercase
import random
import json

question_file = open("questions.json", "r")
questions = json.load(question_file)


NUM_QUESTIONS_PER_QUIZ = 5

def prepare_questions(questions, num_questions):
    num_questions = min(num_questions, len(questions))
    return random.sample(list(questions.items()), k=num_questions)


def get_answer(question, alternatives):
    labeled_answers = dict(zip(ascii_lowercase, alternatives))

    for label, answer in labeled_answers.items():
        print(f"{label}. {answer}")
        
    while (answer_label := input("Choice? ").lower()) not in labeled_answers:
        print(f"Invalid choice. Please select one of {', '.join(labeled_answers.keys())}.")

    answer = labeled_answers.get(answer_label)
    return labeled_answers[answer_label]


def ask_question(question, alternatives):    
    correct_answer = alternatives[0]
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))
    answer = get_answer(question, ordered_alternatives)
    if answer == correct_answer:
        print("Correct!")
        return 1
    else:
        print(f"The answer is '{correct_answer!r}', not {answer!r}.")
        return 0


# Main program logic starts here
questions = prepare_questions(questions, NUM_QUESTIONS_PER_QUIZ)

num_correct = 0

# Main Loop
for num, (question, answers) in enumerate(questions, start=1):
    print(f"\nQuestion {num}: {question}")
    num_correct += ask_question(question, answers)

print(f"\nYou got {num_correct} correct.")
