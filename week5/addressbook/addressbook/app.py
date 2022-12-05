from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/home")
@app.route("/")
def get_all():
    if request.method == 'GET':
        return "Hello"


