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

    def create(self, email, username, password, cpassword):
        """ Method for creating a user"""
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
                emaillength = len(email)
                if emaillength >= 6 and emaillength <= 50:
                    regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$)"
                    if re.search(regex, email):
                        namelength = len(username)
                        if namelength >= 6 and namelength <= 25:
                            passlength = len(password)
                            if passlength >= 6 and passlength <= 25:
                                if email not in USERS.keys():
                                    if password == cpassword:
                                        USERS[email] = [username, password]
                                        result = email in USERS.keys()
                                        return result
                                    return 8
                                return 7
                            return 6
                        return 5
                    return 4
                return 3
            return 2
        return 1