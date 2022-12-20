import random

class TriviaQuestion:
    def __init__(self, question, category, correctAnswer, difficultyLevel=""):
        self.question = question
        self.category = category
        self.difficultyLevel = difficultyLevel
        self.correctAnswer = correctAnswer
        self.incorrectAnswers = []
        self.shuffledAnswers = []
        self.id = self.correctAnswer

    @property
    def get_id(self):
        return self.id
    @property
    def get_question(self):
        return self.question
    
    @get_question.setter
    def set_question(self,value):
        self.question = value
    
    @property
    def get_category(self):
        return self.category
    
    @get_category.setter
    def set_category(self,value):
        self.category = value
    
    @property
    def get_difficultylevel(self):
        return self.difficultyLevel
    
    @get_difficultylevel.setter
    def set_difficultylevel(self,value):
        self.difficultyLevel = value

    @property
    def get_correctanswer(self):
        return self.correctAnswer
    
    @get_correctanswer.setter
    def set_correctanswer(self,value):
        self.correctAnswer = value
    
    @property
    def get_incorrectanswer(self):
        return self.incorrectAnswers

    @get_incorrectanswer.setter
    def set_incorrectanswer(self,value):
        self.incorrectAnswers.append(value)
    
    def getShuffledAnswers(self):
        
        correctAnswer = self.correctAnswer
        copyOfIncorrectAnswers = self.incorrectAnswers
        self.shuffledAnswers.append(correctAnswer)
        for answer in copyOfIncorrectAnswers:
            self.shuffledAnswers.append(answer)
        return self.shuffledAnswers
    