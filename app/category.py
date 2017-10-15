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
        valid_catname = self.check_category_name(catname)
        if valid_catname != "Field must be between 6 and 30 characters long.":
            if valid_catname != "Category name cannot be blank.":
                size = len(CATS)
                self.catname = valid_catname
                self.email = email
                self.catid = size
                CATS.insert(self.catid, {'catname': self.catname, 
                                         'email': self.email, 'catid': self.catid})
                new_category = CATS[self.catid]
                store_catname = new_category['catname']
                if store_catname == self.catname:
                    return 1
                message = "Failed to create category"
                return message
            return valid_catname
        return valid_catname

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

    def delete_category(self, catid, email):
        """Method to delete the category name"""
        self.catid = int(catid)
        category_to_delete = CATS[self.catid]
        self.catname = category_to_delete['catname']
        self.email = category_to_delete['email']
        if self.email == email:
            CATS.insert(self.catid, {'catname': self.catname,
                                     'email': 'del' + self.email,
                                     'catid': self.catid})
            new_category = CATS[self.catid]
            new_mail = new_category['email']
            if new_mail != self.email:
                self.email = new_mail
                return 1
            message = 'failed to delete'
            return message
        message = "The action is Forbiden"
        return message

    def update_category(self, catname, email, catid):
        """Method to update the category name"""
        size = len(CATS)
        if catid < size:
            store_category = CATS[catid]
            store_catname = store_category['email']
            valid_catname = self.check_category_name(catname)
            if valid_catname != store_catname:
                if valid_catname != "Field must be between 6 and 30 characters long.":
                    if valid_catname != "Category name cannot be blank.":
                        self.catname = valid_catname
                        self.email = email
                        self.catid = int(catid)
                        CATS.insert(self.catid, {'catname': self.catname,
                                                'email': self.email,
                                                'catid': self.catid})
                        updated_category = CATS[self.catid]
                        updated_catname = updated_category['catname']
                        if updated_catname == self.catname:
                            return 1
                        message = "Category Name"
                        return message
                    return valid_catname
                return valid_catname
            message = "The name is still the same"
            return message
        message = "Forbiden!Category does not exist"
        return message

    @staticmethod
    def check_category_name(category_name):
        """ Method to check if category name entered is valid """
        new_category_name = category_name.strip()
        if new_category_name != '':
            catname = re.sub(r'\s+', ' ', new_category_name)
            name_length = len(catname)
            if name_length >= 6 and name_length <= 30:
                valid_catname = catname
                return valid_catname
            message = "Field must be between 6 and 30 characters long."
            return message
        message = "Category name cannot be blank."
        return message
