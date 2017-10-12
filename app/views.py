from flask import render_template, url_for, redirect, request, flash

from app import app
from app.forms import RegistrationForm, LoginForm
from app.user import User

NEWUSER = User()

app.secret_key = 'This is my secret_key'


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        # if form.validate_on_submit():
        email = 'mwangi@mwangi.com'
        password = 'mypassword'
        reg = NEWUSER.login(email, password)
        if reg == 1:
            flash('Welcome')
            return redirect(url_for('index'))
        else:
            error = reg
            return render_template('login.html', form=form, error=error)
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST':
        # if form.validate_on_submit():
        email = 'mwangi@mwangi.com'
        username = 'muthama'
        password = 'mypassword'
        cpassword = 'mypassword'
        reg = NEWUSER.create(email, username, password, cpassword)
        if reg == 1:
            flash('Registration Successfull')
            return redirect(url_for('login'))
        else:
            error = reg
            return render_template('signup.html', form=form, error=error)
    return render_template('signup.html', form=form)
