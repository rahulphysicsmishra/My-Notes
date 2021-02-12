# when function has argument to pass
def start_end_decorator(func):

    def wrapper(*args, **kwargs):
        print('start')
        func(*args, **kwargs)
        print('end')
    return wrapper

@start_end_decorator
def add(x):
    return x + 5

# add = start_end_decorator(add)
add(10)

print('*'* 10)
# if function has some arguments to pass... then we will go like this
def start_end_decorator(func):

    def wrapper(*args, **kwargs):
        print('start')
        res = func(*args, **kwargs)
        print('end')
        return res
    return wrapper

@start_end_decorator
def add(x):
    return x + 5

res = add(10)
print(res)