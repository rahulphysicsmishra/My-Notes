"""
Userdict is a dictionary-like container that acts as a wrapper
around the dictionary objects. This container is used when someone
wants to create their own dict with some modified or new functionality

Syntax
class collections.UserDict([initialdata])

"""

from collections import UserDict

# Creating a dictionary where
# deletion is not allowed
class MyDict(UserDict):

    # Function to stop deletion
    # from dictionary
    def __del__(self):
        raise RuntimeError("Deletion not allowed")

    # Function to stop popitem
    # from Dictionary
    def popitem(self, s = None):
        raise RuntimeError("Deletion not allowed")

    # Function to stop popitem
    # from dictionary
    def popitem(self, s = None):
        raise RuntimeError("Deletion not allowed")

# Driver's code
d = MyDict({'a': 1, 'b': 2, 'c': 3})
d.pop(1)



