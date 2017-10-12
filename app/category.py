""" create category class to enable create, view and delete of categories"""

CATS = []


class Category():
    """
    Category class that contains the methods to craete, View, Update, Delete categories
    """
    def __init__(self, catname=None, email=None, catid=0):
        """
        Initialization of the user class
        """
        self.catname = catname
        self.email = email
        self.catid = catid

    