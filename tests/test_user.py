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
    def test_all_inputs_are_empty(self):
        """ method to test if input fields are empty"""
        result = self.new_user.create('', '', '', '')
        self.assertEqual(1, result, "Input fields empty")
    
    def test_email_is_empty(self):
        """ method to test if email field is empty"""
        result = self.new_user.create('', 'Peter', 'patpass', 'patpass')
        self.assertEqual(1, result, "Input fields empty")

    def test_username_is_empty(self):
        """ method to test if username field is empty"""
        result = self.new_user.create('maua@mail.com', '', 'plutos', 'plutos')
        self.assertEqual(1, result, "Username empty")
    
    def test_password_is_empty(self):
        """ method to test if password field is empty"""
        result = self.new_user.create('maua@mail.com', 'Earths', '', 'plutos')
        self.assertEqual(1, result, "Password empty")
    
    def test_cpassword_is_empty(self):
        """ method to test if cpassword field is empty"""
        result = self.new_user.create('maua@mail.com', 'Earths', 'plutos', '')
        self.assertEqual(1, result, "Confirm Password empty")
    
    
   

    def test_create_user(self):
        """ method to test for success in creating user account"""
        user_details = self.new_user.create(
            'maua@gmail.com', 'Peter', 'patpass', 'patpass')
        self.assertTrue(user_details, "User succesfully created")
    
    
