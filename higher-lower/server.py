from flask import Flask
import random

num = random.randint(0, 9)

app = Flask(__name__)

@app.route('/')
def guess_number():
    return  "<h1> Guess a number between 0 and 9</h1>"\
            "<img src='https://media.giphy.com/media/SWhu7En9hffN1b7mbd/giphy.gif'>"

@app.route('/<int:number>')
def guessing_number(number):
    
    if number < num:
        return  "<h1> to low</h1>"\
            "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif number > num:
        return  "<h1> to high</h1>"\
            "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    else:
        return  "<h1> correct</h1>"\
            "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == "__main__": 
    app.run(debug=True)
