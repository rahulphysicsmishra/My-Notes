org = 5
cpy = org  # this will not make a  real copy, it will create a variable with same reference...it does not a  problem with immutable types but it's bad way of copy
cpy = 6  # it will again create a new variable
print(cpy, org)

print('*' * 10)

# we can't make a copy with assignment operator in mutable data types... it changes the original when we change the copied one

# shallow copy: one level deep, only references of nested child objects
# deep copy: full independent copy

import copy
org1 = [0, 1, 2, 3, 4]
cpy1 = copy.copy(org1)  # we can also say cpy1= org1.copy(), list(org1) or org1[:]...but it helps only on one level deep...
cpy1[0] = -10
print(org1, ':', cpy1)

print('*' * 10)
# for nested list, copy method should be deep
org2 = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
org3 = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
cpy_shallow = copy.copy(org2) # is gonna change the item on original and copied level which is bcos it cannot save original from being affected
cpy_deep = copy.deepcopy(org3)  # it's not gonna affect original list.... only copied will be affected
cpy_shallow[0][1] = -10
cpy_deep[0][1] = -10
print(org2, cpy_shallow)
print(org3, cpy_deep)

print('*' * 10)
# class based example
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee

p1 = Person('Alex', 55)
p2 = Person('Joe', 27)

company = Company(p1, p2)
company_clone = copy.copy(company) # shallow copy
company_clone.boss.age = 56
print(company_clone.boss.age, company.boss.age)  # shallow copy is changing it on original level...we need deep copy

p3 = Person('Thor', 59)
p4 = Person('Tony', 25)
company1 = Company(p3, p4)
company1_deep = copy.deepcopy(company1)
company1_deep.boss.age = 55
print(company1_deep.boss.age, company1.boss.age)  # this is the benefit of deep copy... we change only in copied version..
