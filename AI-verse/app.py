from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Dummy questions database
SAMPLE_QUESTIONS = {
    "science": [
        "What is the chemical symbol for water?",
        "What planet is known as the Red Planet?",
        "What gas do plants absorb from the atmosphere?",
        "Who developed the theory of relativity?",
        "What is the hardest natural substance on Earth?"
    ],
    "technology": [
        "Who founded Microsoft?",
        "What does CPU stand for?",
        "What year was the first iPhone released?",
        "What is the main language used for web pages?",
        "What is AI short for?"
    ],
    "math": [
        "What is 7 x 8?",
        "What is the square root of 64?",
        "What is 12 divided by 3?",
        "What is the value of π (pi) approximately?",
        "What is 9 squared?"
    ]
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_quiz():
    topic = request.form['topic'].lower()
    num_questions = int(request.form['num_questions'])
    difficulty = request.form['difficulty']

    questions = SAMPLE_QUESTIONS.get(topic, [])
    if not questions:
        questions = ["Sorry, no questions available for this topic."]

    selected = random.sample(questions, min(num_questions, len(questions)))

    return render_template('quiz.html', topic=topic.title(),
                           difficulty=difficulty.title(),
                           questions=selected)

if __name__ == '__main__':
    app.run(debug=True)
