"""Test User case """
import string
import random
import unittest
from app.user import User


class TestUser(unittest.TestCase):
    """class to test user case"""
    def setUp(self):
        self.user = User()
        self.username = 'Muthamass'
        self.email = 'muthamass@gmail.com'
        self.password = 'password'
        self.cpassword = 'password'

    def test_create_user(self):
        """ method to test for success in creating user account"""
        new_user = self.user.create(self.email, self.username, self.password, self.cpassword)
        self.assertEqual(1, new_user, "User Not Created")
    
    def test_user_exists(self):
        """ method to test if user exists in the database"""
        self.user.create(self.email, self.username, self.password, self.cpassword)
        result = self.user.check_email_in_db(self.email)
        self.assertEqual(1, result, "User exists")

    def test_email_is_not_blank(self):
        """ method to test if email field has been left blank"""
        new_user = self.user.create('', self.username, self.password, self.cpassword)
        self.assertEqual("Email should not be blank", new_user)

    def test_email_has_trailing_spaces(self):
        """ method to test if email contains trailing spaces"""
        trailling_emails = [' muthamass@gmail.com', 'muthamass@gmail.com ',
                            '  muthamass@gmail.com', ' muthamass@gmail.com ']
        for email in trailling_emails:
            new_user = self.user.create(email, self.username, self.password, self.cpassword)
            self.assertEqual("Email cannot have blank space or tabs", new_user)

    def test_email_is_valid_format(self):
        """ method to test if email address is valid"""
        invalid_emails = ['mutha mass@gmail.com', 'muthamass @gmail.com',
                          'muthamass@gmail', 'muthamass@gmail.',
                          'muthamass@ gmail.com', 'muthamass@gm ail.com'
                          'muthamass@gmail. com', 'muthamass@gmail.c om']
        for email in invalid_emails:
            new_user = self.user.create(email, self.username, self.password, self.cpassword)
            self.assertEqual("Enter a valid email address", new_user)

    def test_email_is_valid_length(self):
        """ method to test if email address is valid length"""
        long_email = ''.join(random.choice(string.ascii_lowercase) for _ in range(101))
        invalid_emails = [long_email, 'ss@ss.com']
        for email in invalid_emails:
            new_user = self.user.create(email, self.username, self.password, self.cpassword)
            self.assertEqual("Email Address should contain max 100 characters", new_user)

    def test_email_has_been_registered(self):
        """ method to test if email has already been registered"""
        second_user = self.user.create(self.email, self.username, self.password, self.cpassword)
        self.assertEqual("Email already used for registration", second_user)

    def test_username_is_not_blank(self):
        """ method to test if username field has been left blank"""
        new_user = self.user.create('steve@gmail.com', '', self.password, self.cpassword)
        self.assertEqual("Username should not be blank", new_user)
    
    def test_username_has_spaces(self):
        """ method to test if username contains trailing spaces"""
        trailling_usernames = [' muthama', 'muthama ', 'muth ama']
        for username in trailling_usernames:
            new_user = self.user.create('steve@gmail.com', username, self.password, self.cpassword)
            self.assertEqual("Username cannot have blank space or tabs", new_user)

    def test_username_is_valid_length(self):
        """ method to test if username is valid length"""
        long_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(26))
        invalid_emails = [long_name, 'short']
        for username in invalid_emails:
            new_user = self.user.create('steve@gmail.com', username, self.password, self.cpassword)
            self.assertEqual("Username should contain min 6 and max 50 characters", new_user)

    def test_password_is_not_blank(self):
        """ method to test if password field has been left blank"""
        new_user = self.user.create('steve@gmail.com', self.password, '', self.cpassword)
        self.assertEqual("Password should not be blank", new_user)
    