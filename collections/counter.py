"""A counter is a sub-class of the dictionary. It is used to keep the count of the
 elements in an iterable in the form of an unordered dictionary where the key represents
 the element in the iterable and value represents the count of that element in the iterable."""


# Syntax -  class collections.Counter([iterable-or-mapping])


# A Python program to show different
# ways to create Counter
from collections import Counter

# With sequence of items
print(Counter(['B', 'B', 'A', 'B', 'C', 'A', 'B',
               'B', 'A', 'C']))

# with dictionary
print(Counter({'A': 3, 'B': 5, 'C': 2}))

# with keyword arguments
print(Counter(A=3, B=5, C=2))

