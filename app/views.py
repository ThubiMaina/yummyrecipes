from flask import render_template, url_for, redirect, request, flash

from app import app
from app.forms import RegistrationForm
from app.user import User

NEWUSER = User()

app.secret_key = 'This is my secret_key'


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login')
def login():
    return render_template("login.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    error = None
    if request.method == 'POST' and form.validate():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        cpassword = form.confirm.data
        reg = NEWUSER.create(email, username, password, cpassword)
        if reg == 1:
            flash('Registration Successfull.Proceed to Login')
            return redirect(url_for('login'))
        else:
            error = reg
            return render_template('index.html', error=error)
    return render_template('signup.html', form=form)
