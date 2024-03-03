#======================= SINGLETON PATTERN PRACTISE ============================================


class Hokage:
    _instance = None
    
    # new functions for class
    # cls is another way of stating self which is more utilized in __new__
    def __new__(cls, name):
        # can use == or is
        if cls._instance is None: 
            # calls methods from parent class - built-in keyword in Python
            cls._instance = super(Hokage, cls).__new__(cls)
            cls._instance._name = name

        return cls._instance
    
    def In_Office(self):
        return self._name


# Instance creation
Naruto = Hokage("Naruto Uzumaki")
Kakashi = Hokage("Kakashi Hatake")

# Output should be True, as both instances point to the same object
print(Naruto is Kakashi)

# Output: Naruto Uzumaki is currently the Hokage of THE VILLAGE HIDDEN IN LEAF
print(f"\n{Naruto.In_Office()} is currently the Hokage of THE VILLAGE HIDDEN IN LEAF")


#===================================EXERCISE 2=============================================

class HokageOffice2:
    _instance = None
    _hokage = None
    
    def __new__(cls, name):
        if cls._instance is None:
            cls._instance = super(HokageOffice2, cls).__new__(cls)
            cls._hokage = name  # Assign the Hokage
        return cls._instance
    
    def meet_hokage(self, visitor_name):
        print(f"\n{visitor_name} is meeting Hokage {self._hokage}\n")


# NEW INSTANCES
hokage_office1 = HokageOffice2("Naruto Uzumaki")
hokage_office2 = HokageOffice2("Kakashi Hatake")

# using meet_hokage def
hokage_office1.meet_hokage("Sasuke")  # Sasuke is meeting Hokage Naruto Uzumaki
hokage_office2.meet_hokage("Sakura")  # Sakura is meeting Hokage Naruto Uzumaki (since there's only one instance)


print(hokage_office1 is hokage_office2)  # True, both variables reference the same instance
