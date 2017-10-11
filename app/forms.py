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

from wtforms import (
    Form, StringField, EmailField, PasswordField, HiddenField,
    TextAreaField, validators
)

