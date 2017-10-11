"""This file defines the classes for the forms inorder to utilize
WTForms for validation
Imports:
>>>Form contains field definitions, delegate validation, take input,
aggregate errors.
>>>Stringfield represents an <input type="text">
>>>Passwordfield represents an <input type="password">
>>>Emailfield represents an <input type="email">
>>>Hiddenfield StringField with a HiddenInput widget.
it renders <input type="hidden">
>>>Validators simply takes an input, verifies it fulfills some criterion,
such as a maximum length for a string and returns
"""

from flask_wtf import Form
from wtforms import (
    StringField, PasswordField, HiddenField,
    TextAreaField, validators
)


class RegistrationForm(Form):
    """Registration form with the following field properties:
    Attributes:
        username: A string representing the user's name.
        email: A string representing the user's unique email address.
        password: A string representing the user's password.
        confirm: A string confirming entered password.
    """
    username = StringField('Username', [
        validators.Length(min=6, max=25),
        validators.InputRequired("Username cannot be blank.")
    ])
    email = StringField('Email Address', [
        validators.Length(min=6, max=50),
        validators.InputRequired("email address cannot be blank."),
        validators.Email("This field requires a valid email address")
    ])
    password = PasswordField('Password', [
        validators.Length(min=6, max=25),
        validators.InputRequired("Password cannot be blank."),
    ])
    confirm = PasswordField('Confirm Password', [
        validators.Length(min=6, max=25),
        validators.InputRequired("Password cannot be blank."),
        validators.EqualTo('password', message='Passwords must match')
    ])

