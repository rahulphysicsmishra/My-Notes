"""Operator overloading means giving extended meaning beyond
their predefined operational meaning. For ex + is used to add
two integers as well as join two strings and merge two lists.
It is achievable because '+' operator is overloaded by int class and
str class. We can't create any new operator, but we can overload
all existing operators.

print(1+2)
print("Geeks" + "for")

print(3*4)
print("Geeks * 4)

Note: - User defined data type(class)

To perform operator overloading, python provide some special
function or magic function that is automatically invoked when
it is associated with that particular operator.

"""

# Python program to overload an binary + operator
class A:
    def __init__(self, a):
        self.a = a

    def __add__(self, other):
        return self.a + other.a

ob1 = A(1)
ob2 = A(2)
ob3 = A("Hari")
ob4 = A("Bol")

print(ob1 + ob2)
print((ob3 + ob4))
