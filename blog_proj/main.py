from flask import Flask, render_template, redirect, url_for, flash, abort, jsonify
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from forms import CommentForm, CreatePostForm, RegisterForm, LoginForm
from flask_ckeditor import CKEditor
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from datetime import date

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

login_manager = LoginManager()
login_manager.init_app(app)

#user loader function
@login_manager.user_loader
def load_user(user_id):
    #we are getting user from db
    return User.query.get(int(user_id))


##CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myblog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    #This will act like a List of BlogPost objects attached to each User. 
    #The "author" refers to the author property in the BlogPost class.
    posts = relationship("BlogPost", back_populates="author")
    comments = relationship("Comment", back_populates="comment_author")

class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)
    #Create Foreign Key, "users.id" the users refers to the tablename of User.
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    author = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="parent_post")
    categorie_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    categorie = relationship("Categorie", back_populates="posts_cat")

class Comment( db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    comment_author = relationship("User", back_populates="comments")
    post_id = db.Column(db.Integer, db.ForeignKey("blog_posts.id"))
    parent_post = relationship("BlogPost", back_populates="comments")

class Categorie( db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    categorie = db.Column(db.String(250), unique=True)
    posts_cat = relationship("BlogPost", back_populates="categorie")



# db.create_all()

#admin only decorator
def admin_only(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.id != 2:
            return abort(403, {"error": "you are unautorized for this action"})
        return f(*args, **kwargs)
    return decorated_function

    
@app.route('/posts/<int:page_num>')
def get_all_posts(page_num):
    posts = BlogPost.query.paginate(per_page=4, page=page_num, error_out=True)
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    categories = Categorie.query.all()
    print(categories)
    return render_template("schmindex.html", all_posts=posts, current_user=current_user, categories = categories)

@app.route('/register', methods=["POST", "GET"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).first():
            # User already exists
            flash("You have already created an account. Log in instead.")
            return redirect(url_for('login'))
        
        password = form.password.data
        hashed_pass = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
        new_user = User(
            email=form.email.data,
            password=hashed_pass,
            name=form.name.data
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return redirect(url_for("get_all_posts", page_num=1))

    return render_template("register.html", form=form, current_user=current_user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        user = User.query.filter_by(email=email).first()

        # email doesn't exist
        if not user:
            flash("That email doesn't exist. Please try again")
            return redirect(url_for('login'))
        # password is incorrect
        elif not check_password_hash(user.password, password):
            flash("Password is incorrect. Please try again")
            return redirect(url_for('login'))
        # email exists and password is correct
        else:
            login_user(user)
            return redirect(url_for("get_all_posts", page_num=1))
    return render_template("login.html", form=form, current_user=current_user)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('get_all_posts', page_num=1))

@app.route("/post/<int:post_id>", methods=["POST", "GET"])
@login_required
def show_post(post_id):
    form = CommentForm()
    requested_post = BlogPost.query.get(post_id)
    print(current_user)
    if form.validate_on_submit():
        new_comment = Comment(
            text = form.comment.data,
            comment_author = current_user,
            parent_post = requested_post
        )
        db.session.add(new_comment)
        db.session.commit()
    return render_template("post-second.html", post=requested_post, current_user=current_user, form=form)

@app.route("/about")
@login_required
def about():
    pass

@app.route("/contact")
@login_required
def contact():
    pass

@app.route("/new-post", methods=["GET", "POST"])
@admin_only
def add_new_post():
    form = CreatePostForm()
    res = form.categories.data
    print(res, type(res))

    if form.validate_on_submit():
        print(form)
        new_post = BlogPost(
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            categorie_id=res,
            date=date.today().strftime("%B %d, %Y"),

        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts", page_num=1))
    
    categories = Categorie.query.all()
    choices = []
    for c in categories:
        choices.append((c.id, c.categorie))
    
    form.categories.choices = choices
    return render_template("make-post.html", form=form, current_user=current_user)

@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
# @admin_only
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title = post.title,
        subtitle = post.subtitle,
        img_url = post.img_url,
        body = post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))

    return render_template("make-post.html", form=edit_form)


@app.route("/delete/<int:post_id>")
# @admin_only
def delete_post(post_id):
    pass


if __name__ == "__main__":   
    app.run(port=5000, debug=True)