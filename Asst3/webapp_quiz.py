# Application to manage the quiz webapp
# Name: Rick Kazman
# Date: Nov. 13, 2026

from flask import Flask, render_template, request, redirect, url_for
 
# Global variables
score = 0
question_number = 0
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Madrid", "London", "Berlin", "Paris"]
    },   
    {
        "question": "What planet is known as the Red Planet?",
        "options": ["Venus", "Saturn", "Jupiter", "Mars"]
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"]
    },    
    ]
max_questions = len(questions)

app = Flask(__name__)

@app.route('/')
def index():
    global score, question_number
    score = 0
    question_number = 0
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    global score, question_number, max_questions, questions

    if request.method == 'POST':
        # Capture the answer from the form
        answer = request.form.get('answer')

        # Check if the answer is correct
        if answer == questions[question_number]['options'][-1]:  # Assuming the last option is correct
            score += 1
        question_number += 1

    if question_number < max_questions:
        # Render the next question
        return render_template('quiz.html', 
                               question=questions[question_number]['question'], 
                               question_number=question_number,
                               options=questions[question_number]['options'])
    else:
        # Quiz is over, redirect to the result page
        return render_template('result.html', score=score, max_questions=max_questions)

@app.route('/result')   
def result():
    # Display the final score
    global score, max_questions
    return render_template('result.html', score=score, max_questions=max_questions)

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
    