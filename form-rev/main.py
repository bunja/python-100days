from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def home():
    
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def receive_data():
    name = request.form["username"]
    pwd = request.form["password"]
    return render_template("gotch.html", name = name, pwd = pwd)
if __name__ == "__main__":
    app.run(debug=True)