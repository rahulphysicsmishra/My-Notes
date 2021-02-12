# Accessing arguments by position

print('{0}, {1}, {2}'.format('a', 'b', 'c'))

list_of_fruits = ['Apple', 'Banana', 'Oranges', 'Mangoes']
print("{0}, {1}, {2}, {3}".format(list_of_fruits[0], list_of_fruits[1], list_of_fruits[2], list_of_fruits[3]))

print("{}, {}".format(list_of_fruits[0], list_of_fruits[1]))
print("{}, {}, {}, {}".format(*list_of_fruits))  # Unpacking list
print("{}, {}, {}, {}".format(*'abcd'))  # Unpacking string
print("{2}, {1}, {0}".format(*list_of_fruits))

print("{0}{1}{0}".format('abra', 'cad'))  # Arguments indices can be repeated

print('*'*100)
# Accessing arguments by name

print("Coordinates: {latitude}, {longitude}".format(latitude='37.24N', longitude='-115.81W'))

coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
print("Coordinates: {latitude}, {longitude}".format(**coord))

print('*'*100)
# Accessing argument's attribute

c = 3-5j
print("The complex number {0} is formed from the real part {0.real} and imaginary part {0.imag}.".format(c))

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        return 'Point({self.x}, {self.y})'.format(self=self)

print(str(Point(3,4)))

print('*'*100)
# Accessing argument's items, replacing %s and %r, datetime

coord1 = (3, 4)
print('X:{0[0]}, Y:{0[1]}'.format(coord1))  # no use of * here bcos int obj is not subscriptable

print("repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2'))

import datetime
d = datetime.datetime.now()
print("{:%Y-%m-%d %H-%M-%S}".format(d))  # see the column before %Y.

print('*'*100)
# format use in loop
fruit_name = ['apple', 'mango', 'curd', 'lemon']
product = ['juice', 'shake', 'lassi', 'tea']

for i in range(len(fruit_name)):
    f = "{} gives {}"
    print(f.format(fruit_name[i], product[i]))

print('*'*100)
#class based example
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person('Rahul', 26)
print("My name is {0.name} and age is {0.age} years old".format(p1))
