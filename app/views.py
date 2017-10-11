from flask import render_template, url_for

from app import app

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/register')
def register():
    return render_template("signup.html")

@app.route('/login')
def login():
    return render_template("login.html")