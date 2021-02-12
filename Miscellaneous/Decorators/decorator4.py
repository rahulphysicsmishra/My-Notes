def start_end_decorator(func):

    def wrapper():
        print('start')
        func()
        print('end')
    return wrapper

@start_end_decorator
def print_name():  # here function has no argument to pass
    print('Alex')

# print_name = start_end_decorator(print_name)
print_name()