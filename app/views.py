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
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        cpassword = request.form['cpassword']
        reg = NEWUSER.create(email, username, password, cpassword)
        if reg == 1:
            flash('Registration Successfull.Proceed to Login')
            return redirect(url_for('login'))
        error = reg
        return redirect(url_for('register'))
    return render_template('signup.html', form=form)
