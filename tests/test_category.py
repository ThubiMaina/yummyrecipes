"""Test Category case """
import string
import random
import unittest
from app.category import Category


class TestCategory(unittest.TestCase):
    """class to test user case"""
    def setUp(self):
        self.category = Category()
        self.catname = 'First Category'
        self.email = 'muthamass@gmail.com'
        self.catid = None

    def test_create_category(self):
        """ method to test for success in creating category name"""
        new_category = self.category.create_category(self.catname, self.email)
        self.assertEqual(1, new_category, "Category Not Created")

    def test_category_name_is_not_blank(self):
        """ method to test if category name field is empty"""
        new_category = self.category.create_category('', self.email)
        self.assertEqual("Category name cannot be blank.", new_category)

    def test_category_name_is_valid_length(self):
        """ method to test if category  name is valid length"""
        long_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(31))
        invalid_names = [long_name, 'short']
        for catname in invalid_names:
            new_category = self.category.create_category(catname, self.email)
            self.assertEqual("Field must be between 6 and 30 characters long.", new_category)

    def test_user_can_view_his_categories(self):
        """ method to test if user can successfully see his categories"""
        view_category = self.category.view_category(self.email)
        self.assertEqual(1, view_category)

    def test_returns_empty_if_user_lacks_categories(self):
        """ method to test if user can view another users category"""
        self.email = 'stephen@gmail.com'
        view_category = self.category.view_category(self.email)
        self.assertEqual("Create your first category here >>>", view_category)

    def test_category_is_successfully_deleted(self):
        """ method to test if user can delete their categories"""
        self.category.create_category(self.catname, self.email)
        category_to_delete = self.category.delete_category(0, self.email)
        self.assertEqual(1, category_to_delete)

    def test_user_can_delete_another_user_category(self):
        """ method to test if user can delete another users category"""
        self.category.create_category(self.catname, 'steve@gmail.com')
        category_to_delete = self.category.delete_category(0, self.email)
        self.assertEqual("The action is Forbideen", category_to_delete)
