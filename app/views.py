from flask import render_template, url_for, redirect, request, flash

from app import app
from app.forms import RegistrationForm

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
    if request.method == 'POST' and form.validate():
        flash('Registration Successfull.Proceed to Login')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)
