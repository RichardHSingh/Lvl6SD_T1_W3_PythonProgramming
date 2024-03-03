#======================= PROTOTYPE PATTERN PRACTISE ============================================

import copy

# Define a base class representing the prototype for creating different types of stuffed animals
class StuffedAnimalPrototype:
    def clone(self):
        pass

# Subclass for a specific type of stuffed animal - Wabbit
class Wabbit(StuffedAnimalPrototype):
    # Override the clone method to create a shallow copy of the instance
    def clone(self):
        return copy.copy(self)

# Subclass for another type of stuffed animal - Plushy
class Plushy(StuffedAnimalPrototype):
    # Override the clone method to create a shallow copy of the instance
    def clone(self):
        return copy.copy(self)

# Subclass for a third type of stuffed animal - Figurine
class Figurine(StuffedAnimalPrototype):
    # Override the clone method to create a shallow copy of the instance
    def clone(self):
        return copy.copy(self)

# Create instances of each prototype
wabbitPrototype = Wabbit()
plushyPrototype = Plushy()
figurinePrototype = Figurine()

# Create an empty list to store cloned stuffed animals
stuffed_animal = []

# Clone 10 instances of the Wabbit prototype and add them to the list
for _ in range(10):
    stuffed_animal.append(wabbitPrototype.clone())

# Clone 5 instances of the Plushy prototype and add them to the list
for _ in range(5):
    stuffed_animal.append(plushyPrototype.clone())

# Clone 4 more instances of the Figurine prototype and add them to the list
for _ in range(4):
    stuffed_animal.append(figurinePrototype.clone())

# Display the cloned stuffed animals along with their indices
for idx, animal in enumerate(stuffed_animal, start=1):
    print(f"Stuffed Animal {idx}: {animal}")
