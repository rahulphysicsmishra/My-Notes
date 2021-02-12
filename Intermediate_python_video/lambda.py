# lambda arguments: expression

add10 = lambda x: x + 10  # def add10_func(x): return x + 10
print(add10(5))

mult = lambda x,y: x * y  # def mult_func(x,y): return x * y
print(mult(2, 7))

# lambda function in sorted method
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D)

print(points2D)
print(points2D_sorted)  # By default, it sorts in  ascending x order

points2D_sorted2 = sorted(points2D, key=lambda x: x[1])  # sorted in order of ascending y
print(points2D_sorted2)

points2D_sorted3 = sorted(points2D, key= lambda x: x[0] + x[1])
print(points2D_sorted3)

print('*'*20)
# lambda function in map(map(func, seq))
a = [1, 2, 3, 4, 5]
b = map(lambda x: x*2, a)  #list comp is easier than map.. c = [x*2 for x in a]
print(list(b))

# filter function (filter(func, seq))
a1 = [1, 2, 3, 4, 5, 6]
b1 = filter(lambda x: x%2==0, a1)  # in list comp, c = [x for x in a1 if x%2==0]
print(list(b1))

# reduced function (reduce(func, seq))
from functools import reduce
a2 = [1, 2, 3, 4, 5, 6]
product_a = reduce(lambda x,y: x*y, a2)
print(product_a)

