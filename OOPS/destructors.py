"""Destructors are called when an object gets destroyed. In python, destructors
are not needed as much needed in C++ because Python has a garbage collector that
handles memory management automatically.

Syntax
def __del__(self):
    # body of destructor

Note: A reference to objects is also deleted when the object goes out of reference
or when the program ends.
"""

# Python program to illustrate destructor
class Employee:

    # Initializing
    def __init__(self):
        print('Employee created.')

    # Deleting (calling destructor)
    def __del__(self):
        print('Destructor called, Employee deleted')


obj = Employee()
del obj
# Note: The destructor was called after the program ended or when all the references
# to object are deleted i.e. when the reference  count becomes zero, not when object
# went out of scope.