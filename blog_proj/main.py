from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

app = Flask(__name__)
Bootstrap(app)

##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myblog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

# db.create_all()
    
@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()

    print(posts)
    return render_template("index.html", all_posts=posts)

@app.route('/register', methods=["POST", "GET"])
def register():
    pass

@app.route('/login', methods=['GET', 'POST'])
def login():
    pass

@app.route('/logout')
def logout():
    pass

@app.route("/post/<int:post_id>", methods=["POST", "GET"])
# @login_required
def show_post(post_id):
    requested_post = BlogPost.query.get(post_id)
    return render_template("post.html", post=requested_post)

@app.route("/about")
def about():
    pass

@app.route("/contact")
def contact():
    pass

@app.route("/new-post", methods=["GET", "POST"])
# @admin_only
def add_new_post():
    pass

@app.route("/edit-post/<int:post_id>")
# @admin_only
def edit_post(post_id):
    pass

@app.route("/delete/<int:post_id>")
# @admin_only
def delete_post(post_id):
    pass

if __name__ == "__main__":   
    app.run(port=5000, debug=True)