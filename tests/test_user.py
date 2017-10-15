"""Test User case """

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
        result = self.user.check_email_in_db(self.email)
        self.assertEqual(1, result, "User exists")

    def test_email_is_blank(self):
        """ method to test if email field has been left blank"""
        new_user = self.user.create('', self.username, self.password, self.cpassword)
        self.assertEqual("Email should not be blank", new_user)

    def test_email_contains_trailing_spaces(self):
        """ method to test if email contains trailing spaces"""
        new_user = self.user.create(' muthamass@gmail.com ', self.username, self.password, self.cpassword)
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
