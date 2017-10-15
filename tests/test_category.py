"""Test Category case """
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
        """ method to test for success in creating user account"""
        new_category = self.category.create_category(self.catname, self.email)
        self.assertEqual(1, new_category, "Category Not Created")

    def test_category_name_is_not_blank(self):
        """ method to test if username field is empty"""
        new_category = self.category.create_category(self.catname, self.email)
        self.assertEqual("Category name cannot be blank.", new_category)

    def test_category_name_is_valid_length(self):
        """ method to test if username is valid length"""
        long_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(31))
        invalid_names = [long_name, 'short']
        for catname in invalid_names:
            new_category = self.category.create_category(catname, self.email)
            self.assertEqual("Field must be between 6 and 30 characters long.", new_category)