import functools
def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                res = func(*args, **kwargs)
            return res
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def greet(name):
    print(f'Hare {name}')

res = greet('krishna')
