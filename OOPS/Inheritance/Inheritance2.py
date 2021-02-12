"""A child class needs to identify which class is its parent
class. This can be done by mentioning the parent class name
in the definition of the child class."""

# parent class
class Person(object):

    # __init__ is known as constructor
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

# child class
class Employee(Person):

    def __init__(self, name, idnumber, salary, post):
        self.salary = salary
        self.post = post

        # invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)

# creation of an object variable or an instance
a = Employee('Rahul', 886012, 25000, 'Manager')

# calling a function of the class Person using its instance
a.display()

# 'a' is the instance created for the class Person. It invokes the __init__()
# of the referred class. Since the class Employee inherits from class Person,
# 'name' and 'idnumber' are also the objects of class Employee.