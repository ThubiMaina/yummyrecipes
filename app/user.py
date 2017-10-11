""" create user accounts and enable user to login"""
import re

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
        
        if email != '' and username != '' and password != '' and cpassword != '':
            newmail = email.strip()
            newname = username.strip()
            newpass = password.strip()
            newcpass = cpassword.strip()
            if (
                len(newmail) == len(email) and
                len(newname) == len(username) and
                len(newpass) == len(password) and
                len(newcpass) == len(cpassword)
            ):
                regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$)"
                if re.search(regex, email):
                    nameLength = len(username)
                    if nameLength >= 6 and namelength <= 25:
                        passlength = len(password)
                        if passLength >= 6 and passlength <= 25:

                        return 5
                    return 4
                    if email not in USERS.keys():
                        if password == cpassword:
                    
                    return 4    
                return 3
            return 2
        return 1

