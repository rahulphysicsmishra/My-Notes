# Composition represents part-of relationship
class Salary:  # content
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annual_salary(self):
        return self.pay*12 + self.bonus

class Employee:  # container
    def __init__(self, name, age, pay, bonus):
        self.name = name
        self.age = age
        self.obj_salary = Salary(pay, bonus)

    def total_salary(self):
        return self.obj_salary.annual_salary()

emp = Employee("Rahul", 26, 15000, 10000)
print(emp.total_salary())