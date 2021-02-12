# Hybrid consists of multiple type of inheritance
class School:
    def func1(self):
        print("This func is in school")

class Student1(School):
    def func2(self):
        print("This func is in student1")

class Student2(School):
    def func3(self):
        print("This func is in student2")

class Student3(Student1, School):
    def func4(self):
        print("This func is in Student3")

# Driver's code
object = Student3()
object.func1()
object.func2()
object.func4()

