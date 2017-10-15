""" create category class to enable create, view and delete of categories"""
import re


CATS = []


class Category():
    """
    Category class that contains the methods to craete, View, Update, 
    Delete categories
    """
    def __init__(self):
        """ Initialization of the category class """
        self.user_categories = []
        self.catname = None
        self.email = None
        self.catid = None

    def create_category(self, catname, email):
        """ Method for creating a categories"""
        self.catname = self.check_category_name(catname)
        if self.catname == 1:
            size = len(CATS)
            self.email = email
            self.catid = size
            CATS.insert(self.catid, {'catname': self.catname, 'email': self.email, 'catid': self.catid})
            new_category = CATS[self.catid]
            result = new_category['catname']
            if result == self.catname:
                return 1
            message = "Failed to create category"
            return message
        return self.catname

    def view_category(self, email):
        """Method to view the categories using the session email address"""
        self.email = email
        user_categories = []
        for listvalue in CATS:
            for key in listvalue:
                if listvalue[key] == self.email:
                    user_categories.append(listvalue)
        self.user_categories = user_categories
        if len(self.user_categories) >= 1:
            return 1
        message = "Create your first category here >>>"
        return message


    @staticmethod
    def check_category_name(category_name):
        """ Method to check if category name entered is valid """
        new_category_name = category_name.strip()
        if new_category_name != '':
            catname = re.sub(r'\s+', ' ', new_category_name)
            name_length = len(catname)
            if name_length >= 6 and name_length <= 30:
                return 1
            message = "Field must be between 6 and 30 characters long."
            return message
        message = "Category name cannot be blank."
        return message
