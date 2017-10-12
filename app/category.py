""" create category class to enable create, view and delete of categories"""

CATS = []


class Category():
    """
    Category class that contains the methods to craete, View, Update, Delete categories
    """
    def __init__(self):
        """
        Initialization of the category class
        """
        self.catname = None
        self.email = None
        self.catid = None

    def create_category(self, catname, email):
        """ Method for creating a categoris"""
        size = len(CATS)
        self.catname = catname
        self.email = email
        self.catid = size
        CATS.insert(self.catid, {'catname': self.catname, 'email': self.email, 'catid': self.catid})
        return CATS

    def view_category(self, email):
        """View method to view the categories"""
        mycats = []
        self.email = email
        for listvalue in CATS:
            for key in listvalue:
                if listvalue[key] == self.email:
                    mycats.append(listvalue)
        return mycats

    @staticmethod
    def delete_category(catid):
        """Delete the category from the global list"""
        CATS.pop(catid)

    def update_category(self, catname, email, catid):
        """Update the category with the new inputs"""
        self.catid = catid
        return CATS.insert(self.catid, {'catname': catname, 'email': email, 'catid': self.catid})
