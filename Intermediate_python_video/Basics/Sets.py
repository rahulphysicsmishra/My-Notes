# Sets: unordered, mutable, no duplicates

myset = set()
myset.add(1)
myset.add(2)
myset.add(3)

myset.remove(3)  # if element is invalid, throw keyerror
myset.discard(4)  # works as remove but does not throw error if the element is not valid

myset.pop()  # remove arbitrary element
print(myset)
myset.clear()  # to clear everything
print(myset)

# Some operations, union, intersection etc

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

i = odds.intersection(evens)
print(i)
i2 = odds.intersection(primes)
print(i2)

# operation od difference
setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}
diff = setA.difference(setB)
print(diff)
diff2 = setB.difference(setA)
print(diff2)

sym_diff = setB.symmetric_difference(setA)
print(sym_diff)
sym_diff2 = setA.symmetric_difference(setB)
print(sym_diff2)

print("setA is : ", setA)
setA.update(setB)  # Update a set with the union of itself and others
print("After updating B in A is: ", setA)

print("Before intersection update of B in A: ", setA)
setA.intersection_update(setB)  # Update a set with the intersection of itself and another
print("After intersection update, A is : ", setA)

print("Before difference update of B in A: ", setA)
setA.difference_update(setB)  # remove all element of another set from this set
print("after difference update: ", setA)

print("Before symmetric diff of B in A is: ", setA)
setA.symmetric_difference_update(setB)
print("After symm difference: ",setA)

# subset function
set_subA = {1, 2, 3, 4, 5, 6}
set_subB = {1, 2, 3}

print(set_subA.issubset(set_subB))
print(set_subB.issubset(set_subA))  # report whether another set contain this set

print(set_subA.issuperset(set_subB))  # report whether this set contain another set
print(set_subB.issuperset(set_subA))

print(set_subA.isdisjoint(set_subB))  # return true if both set has null intersection
print(set_subB.isdisjoint(set_subA))

# frozen set

a = frozenset([1,2,3,4])
a.add(2)  # this will give error... you can't modify frozenset
print(a)