#======================= SINGLETON PATTERN EXAMPLE ============================================

class PresidentOffice:
    _instance = None
    _president = None
 
 # creating a new method/function 
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PresidentOffice, cls).__new__(cls)
            cls._president = "John Doe"  # Assign the President
        return cls._instance
 
    def meet_president(self, visitor_name):
        print(f"{visitor_name} is meeting President {self._president}\n")
 

# office 1 = cause instance is currently none, super(presidentOffice) is now implemented
# office 2 = office 2 = office 1 because instance is no longer "NONE"
office1 = PresidentOffice()
office2 = PresidentOffice()
 
office1.meet_president("Alice")  # Alice is meeting President John Doe
office2.meet_president("Bob")    # Bob is meeting President John Doe
 
print(office1 is office2)  # True, both variables reference the same instance
 
 