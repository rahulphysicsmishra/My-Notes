"""In python, functions are the first class objects,

1. Functions are objects; they can be referenced to, passed to
a variable and returned from other functions as well.

2. Functions can be defined inside another function and can also
be passed as an argument to another function.

Decorators allow us to modify the behavior of function or class.
It allows us to wrap another function in order to extend the
behavior of wrapped function, without permanently modifying it.

In decorators, functions are taken as argument into another
function and then called inside the wrapper function.

Syntax:

@gfg_decorator
def hello_decorator():
    print("Gfg")

hello_decorator = gfg_decorator(hello_decorator)

gfg_decorator function is the callable function, will add some
code on top of another callable function hello_decorator function
and return the wrapper function.
"""

# defining a decorator
def hello_decorator(func):

    # inner1 is a wrapper function in which the argument is called
    # inner function can access the outer local functions like in this case "func"
    def inner1():
        print("Hello, this is before function execution")

        #calling the actual function now inside the wrapper function
        func()

        print("This is after function execution")

    return inner1

# defining a function, to be called inside wrapper
def function_to_be_used():
    print("This is inside the function !!")

# passing 'function_to_be_used' inside the
# decorator to control its behavior
function_to_be_used = hello_decorator(function_to_be_used)

# calling the function
function_to_be_used()




