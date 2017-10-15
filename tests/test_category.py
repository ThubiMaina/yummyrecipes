"""Test Category case """
import unittest
from app.category import Category


class TestCategory(unittest.TestCase):
    """class to test user case"""
    def setUp(self):
        self.category = Category()
        self.catname = None
        self.email = None
        self.catid = None