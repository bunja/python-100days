from flask import Flask, render_template
import random
from datetime import date
import requests 

app = Flask(__name__)

@app.route('/')
def guess_number():
    random_number = random.randint(1, 10)
    current_year = date.today().year
    return  render_template("index.html", num=random_number, year=current_year)

@app.route('/guess/<name>')
def guess(name):
    gender_res = requests.get(f"https://api.genderize.io?name={name}")
    gender_data = gender_res.json()
    gender = gender_data['gender']
    age_res = requests.get(f"https://api.agify.io?name={name}")
    age_data = age_res.json()
    age = age_data['age']

    return render_template("guess.html", name=name, gender=gender, age=age)

@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/4ac1ac0029c07296a3fb"
    response = requests.get(blog_url)
    all_posts = response.json()
    print(num)
    print(response)
    return render_template("blog.html", posts=all_posts)




if __name__ == "__main__": 
    app.run(debug=True)