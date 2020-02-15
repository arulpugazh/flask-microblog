from app import app
from flask import render_template, redirect, flash, url_for
from app.forms import LoginForm


@app.route("/")
@app.route("/index")
def index():
    user = {'username': 'Arul'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title="Home", user=user, posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        print("sdds")
        flash("Login requested for user {}, remember_me {}".format(form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template("login_form.html", form=form)
