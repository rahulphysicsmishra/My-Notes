# Base class
class Parent:
    def func1(self):
        print("This is func1 in parent class")

# Derived class1
class Child1(Parent):
    def func2(self):
        print("This is func2 in child1")

# Derived class2
class Child2(Parent):
    def func3(self):
        print("This is func3 in child2")

object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()
