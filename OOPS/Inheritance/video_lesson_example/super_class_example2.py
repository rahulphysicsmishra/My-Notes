class Parent:
    def __init__(self, name):
        print('Parent__init__', name)

class Parent2:
    def __init__(self, name):
        print('Parent2__init__', name)

class Child(Parent, Parent2):
    def __init__(self):
        print('Child__init__')
        super().__init__('Hari')  # super does not call 2nd parent class init..
                           # to inherit more than 1 init from different parent class, call manually..

child = Child()
print(Child.__mro__)

# Observe the order of 'mro'... first main child, parent, parent2 then object..