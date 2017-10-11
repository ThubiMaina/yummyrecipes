""" create user accounts and enable user to login"""
import re

USERS = {}


class User():
    """
    User class that contains the methods to craete a user and login the user
    """
    def __init__(self, username=None, email=None, password=None):
        """
        Initialization of the user class
        """
        self.username = username
        self.email = email
        self.password = password

    def check_email(self, email):
        if email != '':
            newmail = email.strip()
            if len(newmail) == len(email):
                emaillength = len(email)
                if emaillength >= 6 and emaillength <= 50:
                    regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$)"
                    if re.search(regex, email):
                        if email not in USERS.keys():
                            return True
                    message = "Enter a valid email"
                    return message
                message = "email length too big"
                return message
            message = "Remove Trailing whitespaces from email"
            return message
        message = "Email should not be blank"
        return message

    def check_password(self, password, cpassword):
        if password != '':
            newpass = password.strip()
            if len(newpass) == len(password):
                passlength = len(password)
                if passlength >= 6 and passlength <= 25:
                    if password == cpassword:
                        return True
                    message "confirm password coreectly"
                    return message
                message = "min 6 and max 25 characters"
                return message
            message = "Remove Trailing whitespaces from password"
            return message
        message = "Password should not be blank"
        return message

    def check_username(self, username):
        if username != '':
            newname = username.strip()
            if len(newname) == len(username):
                namelength = len(username)
                if namelength >= 6 and namelength <= 25:
                    return True
                message = "min 6 and max 25 characters"
                return message
            message = return "Remove Trailing whitespaces from username"
            return message
        message = return "Username should not be blank"
        return message

    def create(self, email, username, password, cpassword):
        """ Method for creating a user"""
        check_email = self.check_email(email)
        if check_email is True:
            check_username = self.check_username(username)
            if check_username is True:
                check_password = self.check_password(password, cpassword)
                if check_password is True:
                    USERS[email] = [username, password]
                    result = email in USERS.keys()
                    if result is True:
                        message = "Registration Successfull"
                        return message
                    message = "Failed to create user"
                    return message
                return check_password
            return check_username
        return check_email
                
    def check_email_in_db(self, email):
        """ Method to check if email is in the db"""
        emails = USERS.keys()
        if email in emails:
            return True
        message = "Email not registered"
        return message

    def login(self, email, password):
        """ Method to check if passwords match"""
        dbdata = self.check_email_in_db(email)
        if dbdata is True:
            dbvalues = USERS[dbdata]
            if password in dbvalues[1]:
                return True
            message = "incorrect password"
            return message
        return dbdata

    






