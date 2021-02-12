"""Inheritance is the capability of one class to derive or
inherit the properties from another class.
Benefits -
1. It provides reusability of a code. It allows us to add
more features to a class without modifying it.
2. It is transitive in nature, which means that if class B
inherits from another class A, then all the subclasses of B
would automatically inherit from class A."""

# Base or super class
class Person(object):

    # Constructor
    def __init__(self, name):
        self.name = name

    # To get name
    def getName(self):
        return self.name

    # To check if this person is an employee
    def isEmployee(self):
        return False


# Inherited or Subclass
class Employee(Person):

    # here we return True
    def isEmployee(self):
        return True

# Driver code
emp = Person("Hari")  # An object of person
print(emp.getName(), emp.isEmployee())

emp = Employee("Bramha")
print(emp.getName(), emp.isEmployee())
