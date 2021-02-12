# Aggregation represent has-a relationship
class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return self.pay*12 + self.bonus

class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.obj_salary = salary

    def total_salary(self):
        return self.obj_salary.annual_salary()

salary = Salary(15000, 10000)  # The associated class have unidirectional property
emp = Employee("Rahul", 26, salary)  # salary is passed in employee..not the other way round
print(emp.total_salary())

# salary and emp are independent... if one object dies, other survive...