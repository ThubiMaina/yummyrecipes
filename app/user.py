""" create user accounts and enable user to login"""

USERS = {}


class User():
    """
    User class that contains the methods to craete a user and login the user
    """
    def __init__(self, username=None, email=None, password=None, cpassword=None):
        """
        Initialization of the user class
        """
        self.username = username
        self.email = email
        self.password = password
        self.cpassword = cpassword

    def create(self, email, username, password, cpassword):
        USERS[email] = [username, password]
        result = email in USERS
        return result
