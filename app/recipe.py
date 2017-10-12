""" create recipe class to enable create, view and delete of recipes"""

RECIPE = []


class Recipe():
    """
    Recipe class that contains the methods to craete, View, Update, Delete
    """

    def __init__(self, recipename=None, ingridients=None, process=None, catid=0, recipeid=0):
        """
        Initialization of the category class
        """
        self.recipename = recipename
        self.ingridients = ingridients
        self.process = process
        self.catid = catid
        self.recipeid = recipeid
        self.myrecipes = []