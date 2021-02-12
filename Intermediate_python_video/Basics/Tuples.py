# Tuples: ordered, immutable, allows duplicate elements

mytuple = "Rahul", "Govind", "Narayan"
print(type(mytuple))

mytuple2 = tuple(["Rahul", "Govind", "Narsimha"])
print(mytuple2)

mytuple3 = ('a', 'p', 'p', 'l', 'e')
print(mytuple3.count('p'))
print(mytuple3.index('a'))
mylist = list(mytuple3)  # we can convert tuple into list
print(mylist)
print(mytuple3[:])
print(mytuple3[::-1])  # To reverse tuple

# Note this method
mytuple4 = "Max", 26, "Boston"
name, age, city = mytuple4
print(name, age, city)

mytuple5 = (0,1,2,3,4,5)
i1, *i2, i3 = mytuple5
print(i1)
print(i2)
print(i3)

# comparison between list and tuple

import sys
import timeit
my_list = [0,1,2,"hello",True]
my_tuple = (0,1,2,"hello",True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000))

