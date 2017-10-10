""" This file intializes a Python module. Without it, Python will not
     recognize the app directory as a module.
"""
# Load Flask
from flask import Flask

# Load the views
from app import views

# Initialize the app
# set instance_relative_config to True,
# use app.config.from_object('config') to load the config.py file.

APP = Flask(__name__, instance_relative_config=True)


# Load the config file
APP.config.from_object('config')
