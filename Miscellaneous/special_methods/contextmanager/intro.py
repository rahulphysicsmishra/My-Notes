"""In any programming language, the usage of resources like file
operations or database connections is very common. But these re
sources are limited in supply. Therefore the main problem lies
in making sure to release these resources after usage. If they
are not released then it will lead to resource leakage and may
cause the system to either slow down or crash.

In python, we use context managers which facilitate the proper
handling of resources to avoid this problem. The most common
way of performing file operations is by using with keyword

# Python program showing a use of with keyword

with open("test.txt") as f:
    data = f.read()


#  example of file management

file_descriptors = []
for x in range(100000):
    file_descriptors.append(open('test.txt', 'w'))

it will cause OSError: too many open files: 'test.txt'


Creating a context manager: When creating context manager using
classes, user need to ensure that the class has the methods:
__enter__() and __exit__(). The __enter__() returns the resource
that needs to be managed and the __exit__() does not return anything
but performs the cleanup operations.

"""

# creating a context manager
class ContextManager():
    def __init__(self):
        print('init method called')

    def __enter__(self):
        print('enter method called')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit method called')

with ContextManager() as manager:
    print('with statement block')


# In this case, contextmanager obj is created. This is assigned
# to the variable after the as keyword i.e. manager. On running
# the above program, the following get executed in sequence
#1. __init__()
#2. __enter__()
#3. statement body within with block
#4. __exit__() [the parameters in this method are used to manage exceptions
