from flask import render_template, request, flash, redirect, url_for
from main_project import app, db, bcrypt
from main_project.forms import RegisterForm, LoginForm
from main_project.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required


# Sample data
posts = [
    {
        'author': 'Robbie Campbell',
        'title': 'Planned website',
        'content': "Let's make a blog!",
        'date_posted': "17 June 2020",
    },
    {
        'author': 'Ron Campbell',
        'title': 'This website',
        'content': "Let's make a blog!",
        'date_posted': "16 June 2020"
    }
]


# The url routes for all of the webpages
@app.route("/")
@app.route("/home/")
def home():
    return render_template("home.html", posts=posts, title="Home")


@app.route("/about/")
def about():
    return render_template("about.html", title="About")


@app.route("/contact/")
def contact():
    return render_template("contact.html", title="Contact")

# The url routes and functions to flash for registration and login forms


@app.route("/register", methods=["GET","POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created, you can now log in!',"success")
        return redirect(url_for('login'))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET","POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash(f'Logged in successfully!', "success")
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash("Login unsuccessful, please check email and password.", "danger")
    return render_template("login.html", title="Login", form=form)

@app.route("/logout")
def logout():
    logout_user()
    flash(f'Logged out successfully!', "success")
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template("account.html", title="Account")