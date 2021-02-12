# A = 10, 20, 30
# print(A, type(A))
# print(dir(A))

# A = 10, 20, 30
# a, b, c = A
# print(a)
# print(b)
# print(c, type(A))

# import sys
# a = "Johnshekar"
# b = a
# print(sys.getrefcount(a))

# def isPrime(n):
#     # Corner cases
#     if (n <= 1):
#         return False
#     if (n <= 3):
#         return True
#
#     # This is checked so that we can skip
#     # middle five numbers in below loop
    # if (n % 2 == 0 or n % 3 == 0):
    #     return False
    #
    # i = 5
    # while (i * i <= n):
    #     if (n % i == 0 or n % (i + 2) == 0):
    #         return False
    #     i = i + 6
    #
    # return True

# print(isPrime(134))

# def fibonaci(n):
#     a = 0
#     b = 1
#     if n < 0:
#         print("incorrect input")
#     elif n == 0:
#         return a
#     elif n == 1:
#         return b
#     else:
#         for i in range(2, n):
#             c = a + b
#             a = b
#             b = c
#         return  b
#
# print(fibonaci(10))

# my_list = [1, 2, 3, 4]
# print('|'.join(str(i) for i in my_list))

# my_dict = {'rahul': 25, 'darsh': 26}
# my_dict2 = {'darpan': 24}
# my_dict.update(my_dict2)
# print(my_dict)

# a = [1, 2, 3, 4, 5, 6]
# div_by_2 = (num for num in a if num%2 == 0)
# for i in div_by_2:
#     print(i)

# k = {}
# a = "I am Singh and I live in singh malay and I like Singh is King movie and here I am"
# a_str = set(a.split())
# print(a_str)
# for item in a_str:
#     k[item] = a.split().count(item)
#
# for item in k:
#     print(item,":", k[item])

# class food():
#
#     def __init__(self, fruit, color):
#         self.fruit = fruit
#         self.color = color
#
#     def show(self):
#         print("fruit is", self.fruit)
#         print("color is", self.color)
#
# f = food("apple", "red")
# f.show()

class company(object):
    trait = "employee"

    def __init__(self, emp_name, emp_id, emp_salary):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.emp_salary = emp_salary

    def over_ride(self, new_salary):
        self.emp_salary = new_salary

class employee(company):

    def __init__(self, emp_name, emp_id, emp_salary, emp_allowance, emp_holiday):
        self.emp_allowance = emp_allowance
        self.emp_holiday = emp_holiday

        company.__init__(self, emp_name, emp_id, emp_salary)




e2 = employee("hari", 123, 2500, 3000, 2)


# print(e1.emp_id)
# print(e1.emp_name)
# print("salary before change is ", e1.emp_salary)
# print(e1.trait)
# e1.over_ride(45000)
# print("salary after override ", e1.emp_salary)






