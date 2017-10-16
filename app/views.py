from flask import render_template, url_for, redirect, request, flash, session

from app import app
from app.forms import RegistrationForm, LoginForm
from app.user import User
from app.category import Category

NEWUSER = User()
NEWCAT = Category()
app.config['SECRET_KEY'] = 'Thisismysecretkey'


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    """A view class to handle user registration"""
    form = RegistrationForm(request.form)
    if request.method == 'POST':
        # get required data
        form = RegistrationForm(request.form)
        if not form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data
            cpassword = form.confirm.data
            reg = NEWUSER.create(email, username, password, cpassword)

            if reg == 1:
                flash('Registration Successfull! you may now login using your username and password')
                return redirect(url_for('login'))

            error = reg
            return render_template('signup.html', form=form, error=error)

        flash('Please correct the errors below')
        return render_template('signup.html', form=form)
    return render_template('signup.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST':
        # get required data
        form = RegistrationForm(request.form)
        if not form.validate():
            email = form.email.data
            password = form.password.data
            login_state = NEWUSER.login(email, password)
            if login_state == 1:
                session['email'] = email
                session['logged_in'] = 1
                flash("Success!! you are now logged in")
                return redirect(url_for('view_category'))
            error = login_state
            return render_template('login.html', form=form, error=error)
        flash('Please correct the errors below')
        return render_template('login.html', form=form)
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
        result = NEWCAT.view_category(email)
        if result == 1:
            mycats = NEWCAT.user_categories
            return render_template('dashboard.html', mycats=mycats)
        flash(result)
        return render_template('dashboard.html')
    return redirect(url_for('login'))


@app.route('/dashboard', methods=['GET', 'POST'])
def add_category():
    if session.get('logged_in') == 1:
        if request.method == 'POST':
            email = session['email']
            catname = request.form['catname']
            result = NEWCAT.create_category(catname, email)
            if result == 1:
                return redirect(url_for('view_category'))
            flash(result)
            return redirect(url_for('view_category'))
        return redirect(url_for('view_category'))
    return redirect(url_for('login'))


@app.route('/dashboard/del', methods=['POST'])
def del_category():
    """ Delete Selected categories by the user"""
    if session.get('logged_in') == 1:
        email = session['email']
        catids = request.form.getlist('catids')
        for catid in catids:
            result = NEWCAT.delete_category(int(catid), email)
        if result == 1:
            flash('Successfully Deleted Category')
            return redirect(url_for('view_category'))
        flash(result)
        return redirect(url_for('view_category'))
    return redirect(url_for('login'))

@app.route('/dashboard/update/', methods=['POST'])
def update_category():
    """ Update Selected category by the user"""
    if session.get('logged_in') == 1:
        categoryname = request.form['catname']
        categoryid = int(request.form['catid'])
        email = session['email']
        result = NEWCAT.update_category(categoryname, email, categoryid)
        if result == 1:
            flash("Your Category has been updated")
            return redirect(url_for('view_category'))
        flash(result)
        return render_template('updatecat.html', catid=categoryid, catname=categoryname)
    return redirect(url_for('login'))


@app.route('/dashboard/update/<int:catid>', methods=['GET'])
def update_category_get(catid):
    """ Link to Update Selected category by the user"""
    catname = NEWCAT.get_category_name(int(catid))
    return render_template('updatecat.html', catid=catid, catname=catname)
