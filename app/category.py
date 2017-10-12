""" create category class to enable create, view and delete of categories"""

CATS = []


class Category():
    """
    Category class that contains the methods to craete, View, Update, Delete categories
    """
    def __init__(self, catname=None, email=None, catid=0):
        """
        Initialization of the category class
        """
        self.catname = catname
        self.email = email
        self.catid = catid

    def create_category(self, catname, email):
        """ Method for creating a categoris"""
        size = len(CATS)
        self.catid = size
        return CATS.insert(self.catid, {'catname': catname, 'email': email, 'catid': size})

    def view_category(self, email):
        """View method to view the categories"""
        mycats = []
        for listvalue in CATS:
            for key in listvalue:
                if email == listvalue[key]:
                    mycats.append(listvalue)
                    return mycats
                return 1

    @staticmethod
    def delete_category(catid):
        """Delete the category from the global list"""
        CATS.pop(catid)

    def update_category(self, catname, email, catid):
        """Update the category with the new inputs"""
        self.catid = catid
        return CATS.insert(self.catid, {'catname': catname, 'email': email, 'catid': self.catid})
