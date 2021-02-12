# to show the beauty of reproducable nature of random numbers.....not good for security purpose

import random

random.seed(1)
print(random.random())
print(random.randint(1, 10))

random.seed(2)
print(random.random())
print(random.randint(1, 10))

random.seed(1)
print(random.random())
print(random.randint(1, 10))

random.seed(2)
print(random.random())
print(random.randint(1, 10))
print("*"*40)
# Use secrets module for password and tokens for security purposes
import secrets

b = secrets.randbelow(10)  #upperbound not included
print(b)

b1 = secrets.randbits(4)  #bits and bytes method, max 1111- 2**3+2**2+2+1, min 0000,(0-15 value).
print(b1)

mylist2 = list("ABCDEFGH")
print(secrets.choice(mylist2))  #choice not reproducable

# if working with arrays, use numpy module

import numpy as np
ar = np.random.rand(3)
print(ar)
ar2 = np.random.rand(3,3)
print(ar2)
ar3 = np.random.randint(0, 10, 3)  # 10 excluded
print(ar3)
ar4 = np.random.randint(0, 10, (3,4))  # for array with higher dimension, use tuple
print(ar4)

arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(arr)
np.random.shuffle(arr)  # it does not shuffle in between
print(arr)

#numpy random generator uses diffeent no generator as compare to python standard library, it also has different seed func
# use numpy random seed method, instead from seed method of random module...
np.random.seed(1)
print(np.random.rand(3,3))
np.random.seed(1)
print(np.random.rand(3,3))

