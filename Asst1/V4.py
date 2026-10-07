# Interactive quiz system, fourth version
# Make a dictionary with the questions and correct answers
# Allow the user to choose the option by its label

questions = {
    "What is the capital of France?": ["Paris", "Toulouse", "Nice", "Avignon"],
    "What is the capital of Germany?": ["Berlin", "Munich", "Hamburg", "Frankfurt"],
    "The Last Supper was painted by which artist?": ["da Vinci", "Michelangelo", "Raphael", "Caravaggio"],
}

for question, answers in questions.items():
    correct_answer = answers[0]
    sorted_answers = sorted(answers)

    for label, answer in enumerate(sorted_answers, start=1):
        print(f"{label}. {answer}")
        
    answer_label = int(input(f"{question} "))
    answer = sorted_answers[answer_label - 1]

    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is '{correct_answer!r}', not {answer!r}.")