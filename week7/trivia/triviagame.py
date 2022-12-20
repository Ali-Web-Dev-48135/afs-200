import requests
import triviaquestion

class TriviaGame():
    def __init__(self):
        self.questions = []

    @property
    def get_questions(self):
        return self.questions
    
    def getQuestions(self):
        try:
            response = requests.get('https://opentdb.com/api.php?amount=5&category=28&difficulty=easy&type=multiple')
        
            response.raise_for_status()

            response_to_json = response.json()
            for question in response_to_json["results"]:
                saveNewQuestion = triviaquestion.TriviaQuestion(question['question'],question['category'],question['correct_answer'])
                for incorrectAnswer in question['incorrect_answers']:
                    saveNewQuestion.incorrectAnswers.append(incorrectAnswer)
                self.questions.append(saveNewQuestion)
            return self.questions

        except requests.exceptions.HTTPError as httperror:
            print(f"HttpError Has Occured {httperror}")
        except requests.exceptions.ConnectionError as connectionError:
            print(f"A connection error has occured {connectionError}")
        except requests.exceptions.Timeout as timeoutError:
            print(f"Timeout error occured {timeoutError}")
        except requests.exceptions.RequestException as requestError:
            print(f"Request error occured {requestError}")

