from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/4ac1ac0029c07296a3fb"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)

@app.route("/blog/<int:blog_id>")
def get_blog(blog_id):
    id = blog_id - 1
    blog_url = "https://api.npoint.io/4ac1ac0029c07296a3fb"
    response = requests.get(blog_url)
    post = response.json()[id]
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
