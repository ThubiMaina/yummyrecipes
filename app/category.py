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

    def create(self, catname, email):
        """ Method for creating a categoris"""
        size = len(CATS)
        CATS.insert(size, {'catname': catname, 'email': email, 'catid': size})

    def view(self, email):
        mycats = []
        for d in CATS:
            for key in d:
                if email == d[key]:
                    mycats.append(d)
                    return mycats
                    for d in mycats
                      
                return 1
                




