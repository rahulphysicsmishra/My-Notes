"""It is a set of predefined methods to enrich classes. ex __init__, __str__

Dunder method let us emulate the behavior of built-in types. For example, to
get the length of string we can call len('string'). But an empty class definition
doesn't support this behavior out ot the box.
"""

# To show how we get error if we don't use dunder method
# class NoLenSupport:
#     pass

# obj = NoLenSupport()
# print(len(obj))  # It gives us typeError: object of type 'NoLenSupport' has no len()

# To fix this, we can add a __len__ dunder method to the class
class LenSupport:
    def __len__(self):
        return 42

obj = LenSupport()
print(len(obj))
