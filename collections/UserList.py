"""
Userlist is a list like container that acts as a wrapper around
the list objects. This is useful when someone wants to create
their own list with some modified or additional functionality.


Syntax
class collections.UserList([list])
"""

# creating a list where
# deletion is not allowed
from collections import UserList
class MyList(UserList):

    # Function to stop deletion
    # from list
    def remove(self, s = None):
        raise RuntimeError("Deletion is not allowed")

    # Function to stop pop from list
    def pop(self, s = None):
        raise RuntimeError("Deletion is not allowed")

# Driver's code
L = MyList([1, 2, 3, 4])

print(("Original List"))

# Inserting to List
L.append(5)
print("After Insertion")
print(L)

# Deleting from list
L.remove()
