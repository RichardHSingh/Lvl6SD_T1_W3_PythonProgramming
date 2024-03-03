# ============================= ANIMAL FACTORY EXAMPLE =============================

# Interface for creating animals
class Animal:
    def speak(self):
        pass

# Concrete implementations of animals
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Interface for creating animal factories
class AnimalFactory:
    def create_animal(self):
        pass

# Concrete factories producing specific animals
class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()

class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()

# Client code using the factories to get and display animal sounds
def get_animal_sound(animal_factory):
    animal = animal_factory.create_animal()
    return animal.speak()

# instances for cat and dog factory with appropriate return for sound they make
dog_factory = DogFactory()
cat_factory = CatFactory()

dog_sound = get_animal_sound(dog_factory)
cat_sound = get_animal_sound(cat_factory)

print(dog_sound)  # Output: Woof!
print(cat_sound)  # Output: Meow!


# ============================= BURGER FACTORY EXAMPLE =============================

# Interface for creating burgers
class Burger:
    def make(self):
        pass

# Concrete implementations of burgers
class CheeseBurger(Burger):
    def make(self):
        return "Cheeseburger"

class VeggieBurger(Burger):
    def make(self):
        return "Veggie Burger"

# Interface for creating burger factories
class BurgerFactory:
    def create_burger(self):
        pass

# Concrete factories producing specific burgers
class CheeseBurgerFactory(BurgerFactory):
    def create_burger(self):
        return CheeseBurger()

class VeggieBurgerFactory(BurgerFactory):
    def create_burger(self):
        return VeggieBurger()

# Client code using the factories to get and display burger types
def get_burger_type(burger_factory):
    burger = burger_factory.create_burger()
    return burger.make()

# instance for burgers --> veggie and cheeseburger
cheese_burger_factory = CheeseBurgerFactory()
veggie_burger_factory = VeggieBurgerFactory()

get_burger_type(cheese_burger_factory)  
get_burger_type(veggie_burger_factory)  

#printing instances
print(get_burger_type(cheese_burger_factory)) # Output: Preparing a Cheeseburger
print(get_burger_type(veggie_burger_factory)) # Output: Preparing a Veggie Burger
