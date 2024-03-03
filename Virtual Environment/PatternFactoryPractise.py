#======================= FACTORY PATTERN PRACTISE ============================================

# Base class for pattern
class Catering:
    def prepare(self):
        pass
    # pass keyword is used when no code is involved inwith the method//function

# Protein sub-class - will print given value with comment
class Protein(Catering):
    def prepare(self):
        print("Preparing protein for todays lunch")

# Carb sub-class - will print given value with comment
class Carb(Catering):
    def prepare(self):
        print("Preparing starch for todays lunch")

# Vege sub-class - will print given value with comment
class Vegetarian(Catering):
    def prepare(self):
        print("Preparing veges for todays lunch")


class Setup:
    def buffet(self, lunch):
        if lunch == "Meat":
            return Protein()
        elif lunch == "Rice":
            return Carb()
        elif lunch == "Veges":
            return Vegetarian()
        else:
            print("Is not on todays menu")

# my instance for setup class
# instances for the subclasses
setup = Setup()

lunchMeat = setup.buffet("Meat")
lunchCarb = setup.buffet("Rice")
lunchVege = setup.buffet("Veges")

# list for catering objects --> come from instances
menu = [lunchMeat, lunchCarb, lunchVege]

for menus in menu:
    menus.prepare()