from flask import Flask, render_template, flash, redirect, url_for
from forms import RegisterForm, LoginForm
from datetime import datetime
import re

# The main loop that runs the website
app = Flask(__name__)
print(" * http://127.0.0.1:5000/about")

################# MUST BE UPDATED ON RELEASE #######################
app.config['SECRET_KEY'] = 'b9457a3518aa6d425fff061cbd1678406698da0dc218abffcd6cc19820a431a8'

# Sample data
posts = [
    {
        'author':'Robbie Campbell',
        'title':'Planned website',
        'content':"Let's make a blog!",
        'date_posted': "17 June 2020",
    },
    {
        'author':'Ron Campbell',
        'title':'This website',
        'content':"Let's make a blog!",
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
@app.route("/register/", methods=["GET","POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!',"success")
        return redirect(url_for('home'))
    return render_template("register.html", title="Register", form=form)

@app.route("/login/", methods=["GET","POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash(f'Logged in successfully!',"success")
            return redirect(url_for('home'))
    else:
        flash("Login unsuccessful, please try again.", "danger")
    return render_template("login.html", title="Login", form=form)
    