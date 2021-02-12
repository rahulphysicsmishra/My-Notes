import functools

def start_end_decorator(func):
    @functools.wraps(func)  # when you call help on add func, it preserves the information of the used function
    def wrapper(*args, **kwargs):
        print('start')
        res = func(*args, **kwargs)
        print('end')
        return res
    return wrapper

@start_end_decorator
def add(x):
    return x + 5


print(help(add))  # without using functools decorator on wrapper, it wont identify the add function
print(add.__name__)