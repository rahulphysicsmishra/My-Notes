import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def set_radius(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def area(self):
        return math.pi * self.get_radius() ** 2

    def __add__(self, other):
        return Circle(self.__radius + other.__radius)

    def __lt__(self, other):
        return (self.__radius < other.__radius)

    def __gt__(self, other):
        return (self.__radius > other.__radius)

    def __str__(self):
        return "Circle area is " + str(self.area())

c1 = Circle(2)
c2 = Circle(3)
c = c1 + c2  # It will give error without using operator overloading __add__ method
# print(c.area())
print(c1.get_radius())
print(c2.get_radius())
print(c.get_radius())

print(c1 > c2)
print(c2 > c1)

print(str(c))