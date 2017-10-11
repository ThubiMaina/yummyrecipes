"""Test User case """

import unittest
from app.user import User


class TestUser(unittest.TestCase):
    """class to test user case"""
    def setUp(self):
        self.new_user = User()
        
        """Creates account successfully,
        check user email available
        inputs blank, Individual field blank-4
        inputs starts with anything other than letter-4
        input has trailling white spaces-4
        password matching.
        invalid email
        min 6.
        max length
        """
    def test_create_user(self):
        """ method to test for success in creating user account"""
        user_details = self.new_user.create(
            'maua@gmail.com', 'Peter', 'patpass', 'patpass')
        self.assertTrue(user_details, "User succesfully created")
    
