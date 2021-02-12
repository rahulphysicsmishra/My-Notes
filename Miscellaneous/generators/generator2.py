# Another example of generator
import sys

def countdown(num):
    print('Starting')
    while num > 0:
        yield num
        num -= 1

cd = countdown(4)
print(next(cd))
print(next(cd))
print(next(cd))
print(next(cd))  # if i print next again, it will throw stop iteration error

# Another example of generator showing memory efficient

def first_n(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

print(sys.getsizeof(first_n(10000)))


def first_n_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1


print(sys.getsizeof(first_n_generator(10000)))  # to show memory management of generators

# fibonacci in generator expression
def fibonacci(limit):
    # 0, 1, 1, 2, 3, 5,..
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b

fib = fibonacci(30)
for i in fib:
    print(i)