import triviagame

from flask import Flask, render_template
from flask import request

app=Flask(__name__)

#Temporary things to be deleted laster.

testTriviaGame = triviagame.TriviaGame()
# Create a new instance of the TriviaGame class and then get questions with randomly ordered answers

gameBoardQuestions = testTriviaGame.getQuestions()

@app.route("/")
def getQuestions():
    return render_template('index.html', questions=gameBoardQuestions)



@app.route('/score', methods=['POST'])
def checkAnswers():
    if request.method == 'POST':
        correctlyAnsweredQuestions = []
        incorrectlyAnsweredQuestions = []
        for question in testTriviaGame.get_questions:
            if (request.form[question.id] == question.correctAnswer):
                correctlyAnsweredQuestions.append(question)
            else:
                incorrectlyAnsweredQuestions.append(question)
        return render_template('results.html', correct=correctlyAnsweredQuestions,incorrect=incorrectlyAnsweredQuestions)


if __name__ == "__main__":
    app.run()