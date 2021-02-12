"""
A NamedTuple returns a tuple object with names for each position which the ordinary tuples lack.
Syntax:

class collections.namedtuple(typename, field_names)

Conversion Operations
1. _make(): This function is used to return a namedtuple() from the iterable passed as argument.

2. _asdict(): This function returns the OrdereDict() as constructed from the mapped values of namedtuple().
"""


# Python code to demonstrate namedtuple()

from collections import namedtuple

# Declaring namedtuple()
Student = namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', '2541997')

# Access using index
print("The Student age using index is : ", end="")
print(S[1])

# Access using name
print("The Student name using keyname is : ", end="")
print(S.name)



# 2nd example

# Python code to demonstrate namedtuple() and
# _make(), _asdict()


from collections import namedtuple

# Declaring namedtuple()
Student = namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', '2541997')

# initializing iterable
li = ['Manjeet', '19', '411997']

# initializing dict
di = {'name': "Nikhil", 'age': 19, 'DOB': '1391997'}

# using _make() to return namedtuple()
print("The namedtuple instance using iterable is : ")
print(Student._make(li))

# using _asdict() to return an OrderedDict()
print("The OrderedDict instance using namedtuple is : ")
print(S._asdict())



