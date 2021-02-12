"""Private members are similar to protected members, the difference is that
the class members declared private should neither be accessed outside the class
nor by any base class. In python, there is no existence of private instance
variables that cannot be accessed except inside the class. (__ underscore for private)

Note: Using python name mangling, we can access private and protected members."""

class Base:
    def __init__(self):
        self.a = "GeekforGeeks"
        self.__c = "GeekforGeeks"

# creating a derived class
class Derived(Base):
    def __init__(self):

        # Calling constructors of Base class
        Base.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)

# Driver code
obj1 = Base()
print(obj1.a)
# print(obj1.__c)

obj2 = Derived()
print(obj2.__c)