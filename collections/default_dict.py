"""A DefaultDict is also a sub-class to dictionary. It is used to provide some
 default values for the key that does not exist and never raises a KeyError."""

# Syntax - class collections.defaultdict(default_factory)

# default_factory is a function that provides the default value
# for the dictionary created. If this parameter is absent then the KeyError is raised.



# Python program to demonstrate
# defaultdict


from collections import defaultdict

# Defining the dict
d = defaultdict(int)

L = [1, 2, 3, 4, 2, 4, 1, 2]

# Iterate through the list
# for keeping the count
for i in L:
    # The default value is 0
    # so there is no need to
    # enter the key first
    d[i] += 1

print(d)



# Python program to demonstrate
# defaultdict


from collections import defaultdict

# Defining a dict
d = defaultdict(list)

for i in range(5):
    d[i].append(i)

print("Dictionary with values as list:")
print(d)
