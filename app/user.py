""" Create user accounts and enable user to login"""
import re

USERS = {}


class User():
    """
    User class that contains the methods to craete a user and login the user
    """
    def __init__(self):
        """ Initialization of the user class """
        self.username = None
        self.email = None
        self.password = None

    def create(self, email, username, password, cpassword):
        """ Method for creating a user"""
        check_email = self.check_email(email)
        if check_email == 1:
            check_username = self.check_username(username)
            if check_username == 1:
                check_password = self.check_password(password, cpassword)
                if check_password == 1:
                    self.email = email
                    self.username = username
                    self.password = password
                    USERS[self.email] = [self.username, self.password]
                    result = self.email in USERS.keys()
                    if result is True:
                        return 1
                    message = "Failed to create user"
                    return message
                return check_password
            return check_username
        return check_email

    def login(self, email, password):
        """ Method to check if passwords match"""
        dbdata = self.check_email_in_db(email)
        if dbdata == 1:
            self.email = email
            self.password = password
            dbvalues = USERS[self.email]
            if self.password in dbvalues[1]:
                return True
            message = "incorrect password"
            return message
        return dbdata

    @staticmethod
    def check_email(email):
        """ Method to check if email entered is valid """
        if email != '':
            newmail = email.strip()
            if len(newmail) == len(email):
                emaillength = len(email)
                if emaillength >= 10 and emaillength <= 100:
                    regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$)"
                    if re.search(regex, email):
                        if email not in USERS.keys():
                            return 1
                        message = "Email already used for registration"
                        return message
                    message = "Enter a valid email address"
                    return message
                message = "Email Address should contain max 100 characters"
                return message
            message = "Email cannot have blank space or tabs"
            return message
        message = "Email should not be blank"
        return message

    @staticmethod
    def check_username(username):
        """ Method to check if username entered is valid """
        if username != '':
            stripname = username.strip()
            newname = re.sub(r'\s+', '', stripname)
            if len(newname) == len(username):
                namelength = len(username)
                if namelength >= 6 and namelength <= 25:
                    return 1
                message = "Username should contain min 6 and max 25 characters"
                return message
            message = "Username cannot have blank space or tabs"
            return message
        message = "Username should not be blank"
        return message

    @staticmethod
    def check_password(password, cpassword):
        """ Method to check if password entered is valid """
        if password != '':
            strippass = password.strip()
            newpass = re.sub(r'\s+', '', strippass)
            if len(newpass) == len(password):
                passlength = len(password)
                if passlength >= 8 and passlength <= 25:
                    if password == cpassword:
                        return 1
                    message = "confirm password coreectly"
                    return message
                message = "Password should contain min 9 and max 25 characters"
                return message
            message = "Password cannot have blank space or tabs"
            return message
        message = "Password should not be blank"
        return message

    @staticmethod
    def check_email_in_db(email):
        """ Method to check if email is in the db"""
        emails = USERS.keys()
        if email in emails:
            return 1
        message = "Email not registered"
        return message
