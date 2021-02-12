class Parent:
    def __init__(self, name):
        print('Parent__init__', name)

class Child(Parent):
    def __init__(self):
        print('Child__init__')
        super().__init__('Hari')

child = Child()
print(Child.__mro__)  # It shows order in which it is called
  # Mro = method resolution order