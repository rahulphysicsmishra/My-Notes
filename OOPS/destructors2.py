# Here destructor is called after 'program end' printed.

class Employee:

    # initializing
    def __init__(self):
        print('Employee created')

    # Calling destructor
    def __del__(self):
        print('Destructor called')

def Create_obj():
    print('Making object...')
    obj = Employee()
    print('function end')
    return obj

print('Calling Create_obj() function...')
obj = Create_obj()
print('Program End...')
