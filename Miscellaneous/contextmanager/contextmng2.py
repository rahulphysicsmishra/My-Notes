# showing exception example of contextmng1

class ManagedFile:
    def __init__(self, filename):
        print('init')
        self.filename = filename

    def __enter__(self):
        print('enter')
        self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print('exception has been handled')
        # print('exc:', exc_type, exc_val)
        print('exit')
        return True  # not to raise exception, we are returning true

with ManagedFile('notes.txt') as file:
    print('do some stuffffff....')
    file.write('soome todoooooooo....')
    file.somemethod()  # just to raise error.....
print('continuing')


# Using function for context manager
from contextlib import contextmanager

@contextmanager
def open_managed_file(filename):
    f = open(filename, 'w')
    try:
        yield f
    finally:
        f.close()

with open_managed_file('notes.txt') as f:
    f.write('some todoooooooooooo.....')