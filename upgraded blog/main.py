from flask import Flask, render_template, request
import requests 
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/4ac1ac0029c07296a3fb"
    response = requests.get(blog_url)
    all_posts = response.json()
    print(all_posts)
    date = datetime.now()
    print(date)
    return render_template("index.html", posts=all_posts, date = date )

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.form
        print(data["username"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return "<h1>Successfully sent your message</h1>"
    return render_template("contact.html")

@app.route("/form-entry", methods=["POST"])
def receive_data():
    



    return render_template("contact.html")

@app.route("/blog/<int:blog_id>")
def get_blog(blog_id):
    id = blog_id - 1
    blog_url = "https://api.npoint.io/4ac1ac0029c07296a3fb"
    response = requests.get(blog_url)
    post = response.json()[id]
    return render_template("post.html", post=post)



if __name__ == "__main__":
    app.run(debug=True)