"""A class is a user-defined blueprint or prototype from which objects are created.
Classes provide a means of bundling data and functionality together. Creating a new
class creates a new type of object, allowing new instances of that type to be made.
Each class instance can have attributes attached to it for maintaining its state.
Class instances can also have methods (defined by its class) for modifying its state."""

class Dog:

    # Class variable
    animal = 'dog'

    # The init menthod or constructor
    def __init__(self, breed, color):

        # Instance variable
        self.breed = breed
        self.color = color

# Objects of Dog class
Rodger = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")

print('Rodger details: ')
print('Rodger is a', Rodger.animal)
print('Breed:', Rodger.breed)
print('Color:', Rodger.color)

print('\nBuzo details: ')
print('Buzo is a', Buzo.animal)
print('Breed:', Buzo.breed)
print('Color:', Buzo.color)

# Class variables can be accessed using class name also
print("\nAccessing class variables using class name")
print(Dog.animal)
