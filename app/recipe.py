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

    def create_recipe(self, catid, recipename, ingridients, process):
        """ Method for creating a recipes for a particular category"""
        size = len(RECIPE)
        self.recipeid = size
        return RECIPE.insert(self.recipeid, {
            'catid': catid,
            'recipeid': self.recipeid,
            'recipename': recipename,
            'ingridients': ingridients,
            'process': process
        })

    def view_recipe(self, recipeid):
        """View method to view the recipes"""
        myrecipes = []
        for listvalue in RECIPE:
            for key in listvalue:
                if recipeid == listvalue[key]:
                    myrecipes.append(listvalue)
                    return myrecipes
                return 1

    @staticmethod
    def delete_recipe(recipeid):
        """Delete the recipe from the global list"""
        RECIPE.pop(recipeid)

    def update_recipe(self, catid, recipeid, recipename, ingridients, process):
        """Update the recipe with the new inputs"""
        self.recipeid = recipeid
        return RECIPE.insert(self.recipeid, {
            'catid': catid,
            'recipeid': recipeid,
            'recipename': recipename,
            'ingridients': ingridients,
            'process': process
        })
