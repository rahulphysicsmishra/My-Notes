"""
A ChainMap encapsulates many dictionaries into a single unit and returns a list of dictionaries.

Syntax:

class collections.ChainMap(dict1, dict2)
"""

# ex- 1
# Python program to demonstrate
# ChainMap


from collections import ChainMap

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

# Defining the chainmap
c = ChainMap(d1, d2, d3)

print(c)



#ex - 2
# Python program to demonstrate
# ChainMap


from collections import ChainMap

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

# Defining the chainmap
c = ChainMap(d1, d2, d3)

# Accessing Values using key name
print(c['a'])

# Accesing values using values()
# method
print(c.values())

# Accessing keys using keys()
# method
print(c.keys())





# ex-3
# Python code to demonstrate ChainMap and
# new_child()

import collections

# initializing dictionaries
dic1 = {'a': 1, 'b': 2}
dic2 = {'b': 3, 'c': 4}
dic3 = {'f': 5}

# initializing ChainMap
chain = collections.ChainMap(dic1, dic2)

# printing chainMap
print("All the ChainMap contents are : ")
print(chain)

# using new_child() to add new dictionary
chain1 = chain.new_child(dic3)

# printing chainMap
print("Displaying new ChainMap : ")
print(chain1)
