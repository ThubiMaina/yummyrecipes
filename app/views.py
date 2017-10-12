from flask import render_template, url_for, redirect, request, flash, session

from app import app
from app.forms import RegistrationForm, LoginForm
from app.user import User
from app.category import Category

NEWUSER = User()
NEWCAT = Category()

app.secret_key = 'This is my secret_key'


@app.route('/check')
def test():
    email = "muthoni"
    ctname = 'kamau'
    cat2 = 'otieno'
    NEWCAT.create_category(ctname, email)
    NEWCAT.create_category(cat2, email)
    mycats = NEWCAT.view_category(email)
    return render_template("checkcat.html", mycats=mycats)

@app.route('/')
def index():
    return render_template("index.html")


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        # if form.validate_on_submit():
        email = 'mwangi@mwangi.com'
        password = 'mypassword'
        reg = NEWUSER.login(email, password)
        if reg == 1:
            session['email'] = email
            session['logged_in'] = 1
            flash("Welcome back")
            return redirect(url_for('view_category'))
        else:
            error = reg
            return render_template('login.html', form=form, error=error)
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    '''remove session stored values if any'''
    session.pop('email', None)
    session.pop('logged_in', 0)
    return redirect(url_for('index'))


@app.route('/dashboard', methods=['GET'])
def view_category():
    if session.get('logged_in') == 1:
        email = session['email']
        mycats = NEWCAT.view_category(email)
        if mycats != 1:
            return render_template('dashboard.html', mycats=mycats)
        return render_template('index.html')
        '''mycats = [
            {'catname': 'Albert', 'email': 2, 'catid': 10},
            {'catname': 'Suzy', 'email': 2, 'catid': 17}
        ]
        return render_template('dashboard.html', mycats=mycats)'''
    return redirect(url_for('login'))


@app.route('/dashboard', methods=['GET', 'POST'])
def add_category():
    if session.get('logged_in') == 1:
        if request.method == 'POST':
            email = session['email']
            catname = request.form['catname']
            NEWCAT.create_category(catname, email)
            return redirect(url_for('view_category'))
        return redirect(url_for('view_category'))
    return redirect(url_for('login'))
