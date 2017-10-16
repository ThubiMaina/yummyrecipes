"""Test Category case """
import string
import random
import unittest
from app.category import Category
from app.category import CATS


class TestCategory(unittest.TestCase):
    """class to test user case"""
    def setUp(self):
        self.cats = CATS
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

    def test_category_name_length(self):
        """ method to test if category  name is valid length"""
        long_name = ''.join(random.choice(string.ascii_lowercase) for _ in range(31))
        invalid_names = [long_name, 'short']
        for catname in invalid_names:
            new_category = self.category.create_category(catname, self.email)
            self.assertEqual("Field must be between 6 and 30 characters long.", new_category)

    def test_view_categories(self):
        """ method to test if user can successfully see his categories"""
        self.category.create_category(self.catname, self.email)
        view_category = self.category.view_category(self.email)
        self.assertEqual(1, view_category)

    def test_view_empty_categories(self):
        """ method to test what happens if user has no categories"""
        self.email = 'stephen@gmail.com'
        view_category = self.category.view_category(self.email)
        self.assertEqual("Create your first category here >>>", view_category)

    def test_delete_categories(self):
        """ method to test if user can delete their categories"""
        category_to_delete = self.category.delete_category(0, self.email)
        self.assertEqual(1, category_to_delete)

    def test_delete_foreign_category(self):
        """ method to test if user can delete another users category"""
        category_to_delete = self.category.delete_category(0, self.email)
        self.assertEqual("The action is Forbiden", category_to_delete)

    def test_update_category(self):
        """ method to test if user can update their category successfully"""
        size = len(self.cats)
        self.category.create_category(self.catname, self.email)
        category_update = self.category.update_category('update category', self.email, size)
        self.assertEqual(1, category_update)

    def test_update_same_name_category(self):
        """ method to test if user can update their category with the same name"""
        category_update = self.category.update_category('update category', self.email, 1)
        self.assertEqual("The name is still the same", category_update)

    def test_update_foreign_category(self):
        """ method to test if user can update a foreign category"""
        category_update = self.category.update_category('foreign category', 'steve@gmail.com', 1)
        self.assertEqual("Forbiden! Action Not allowed", category_update)

    def test_update_outofrange_category(self):
        """ method to test if user can update out of range category"""
        category_update = self.category.update_category('foreign category', 'steve@gmail.com', 20)
        self.assertEqual("Forbiden! Category does not exist", category_update)

    def test_update_invalid_category(self):
        """ method to test if user can update blank category"""
        category_update = self.category.update_category('   ', self.email, 1)
        self.assertEqual("Category name cannot be blank.", category_update)

    def test_update_short_category(self):
        """ method to test if user can update out of range category"""
        category_update = self.category.update_category('short', self.email, 1)
        self.assertEqual("Field must be between 6 and 30 characters long.", category_update)
