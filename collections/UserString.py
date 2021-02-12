"""
UserString is a string like container and just like UserDict
and UserList, it acts as a wrapper around string objects. it
is used when someone wants to create their own strings with
some modified or additional functionality.

Syntax
class collections.UserString(seq)

"""
# Creating a Mutable String
from collections import UserString
class Mystring(UserString):

    # Function to append a string
    def append(self, s):
        self.data += s

    # Function to remove from string
    def remove(self, s):
        self.data = self.data.replace(s, "")

# Driver's code
s1 = Mystring("Geeks")
print("Original String: ", s1.data)

# Appending to string
s1.append("s")
print("String after appending: ", s1.data)

# removing from string
s1.remove("e")
print("String after removing: ", s1.data)
