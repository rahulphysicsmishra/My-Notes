def foo(a, b, *args, **kwargs):
    # *args- any no of poitional args
    # **kwargs- any no of keyword args
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

foo(1, 2, 3, 4, 5, six=6, seven=7)

# example of forced keyword arg
def fooo(a, b, *, c, d):  # every other arg after * should be keyword arg
    print(a, b, c, d)

fooo(1, 2, c = 3, d = 4)  #parameter and keyword should be same

print('*' * 10)

def foooo(*args, last):  # after *args, all parameter should be keyword parameter
    for arg in args:
        print(arg)
    print(last)

foooo(1, 2, 3, last=4)

print('*' * 10)

# unpacking elements
def fo(a, b, c):
    print(a, b, c)

my_list = [1, 2, 3]  # no of items in container shoul be equal to no of parameters in function
my_dict = {'a': 1, 'b': 2, 'c': 3}
fo(*my_list)  # we can use list, tuple, dict as containers...
fo(**my_dict)  # in dict, keys and parameter should match by name and length


print('*' * 10)
# immutable objects cannot be changed
def fun(x):
   x = 5

var = 10  # global variable
fun(var)
print(var)


print('*' * 10)
# mutable objects can be changed
def funn(a_list):
   a_list.append(4)

my_list1 = [1, 2, 3]  # global variable
funn(my_list1)
print(my_list1)

print('*' * 10)
def func(list1):
    list1 += [100, 200, 300]  # it will add to the global list..
    # list1 = list1 + [100, 200, 300]  # it will not modify global list bcos it is creating local variable

mylist = [1, 2, 3]
func(mylist)
print(mylist)

print('*' * 10)
# Unpacking list
numbers = [1, 2, 3, 4, 5, 6]  # if it is tuple, it still works, but unpack will return in the form of list
*beginning, last = numbers
print(beginning, ':', last)  # it will unpack in a list, but if u print *beginning, it will open list
begin, *lastt = numbers
print(begin,':', lastt)

print('*' * 10)
# tuple + list unpacking example and merging into a list
my_tup = (1, 2, 3)
my_lis = [4, 5, 6]

new_list = [*my_tup, *my_lis]  # making new list after unpacking tuple and list
print(new_list)
new_set = {*my_tup, *my_lis}  # making new set after unpacking tuple and list
print(new_set)

print('*' * 10)
# merging dict after unpack
dict_a = {'a': 1, 'b': 2}
dict_b = {'c': 3, 'd': 4}
my_dic = {**dict_a, **dict_b}
print(my_dic)
