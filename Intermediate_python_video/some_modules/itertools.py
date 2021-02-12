from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby

# Product examples
a = [1, 2]
b = [3, 4]
prod = product(a, b)
print(list(prod))

a1 = [1, 2]
b1 = [3]
prod2 = product(a1, b1, repeat= 2)
print(list(prod2))


# Permutation examples
a2 = [1, 2, 3]
perm = permutations(a2)
perm2 = permutations(a2, 2)
print(list(perm))
print(list(perm2))


# combination and combination with replacement examples
a3 = [1, 2, 3, 4]
comb = combinations(a3, 1)
comb2 = combinations(a3, 2)
comb_rep = combinations_with_replacement(a3, 2)
print(list(comb))
print(list(comb2))
print(list(comb_rep))


# accumulate example
import  operator
a4 = [1, 2, 3, 4]
a5 = [1, 2, 5, 3, 1]
acc = accumulate(a4)
acc2 = accumulate(a4, func=operator.mul)
acc3 = accumulate(a5, func=max)
print(a4)
print(list(acc))
print(list(acc2))
print(list(acc3))


# group by function examples

def smaller_than_3(x):  # in lambda, (lambda x: x < 3)
    return x < 3

a6 = [1, 2, 3, 4]
group_obj = groupby(a6, key= smaller_than_3)
for key, value in group_obj:
    print(key, list(value))

# another example of group by
persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
           {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]

group_obj2 = groupby(persons, key= lambda x: x['age'])
for key, value in group_obj2:
    print(key, list(value))

# In infinite iterators, there are 3 functions, count, cycle, and repeat
# count function - makes infinite loop, let's say if we print i in for i in count(10)..
# it will print from 10 to infinite with gap 1...

# cycle function - makes infinite cycle.... ex - for in cycle(a) where a = [1,2,3]... gives infinite cycle of 1,2,3.

# repeat function - gives repetition of number we want as many times...
# a =[1,2,3] for i in repeat(1, 4) times gives 1111.


