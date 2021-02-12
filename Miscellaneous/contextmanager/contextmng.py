# First how to use with statement and difference between normal file opening or with using 'with'

with open('notes.txt', 'w') as file:  # shortcut with statement
    file.write('some todooo.....')

# normally we proceed like this
file = open('notes.txt', 'w')
try:
    file.write('some todoo.....')
finally:
    file.close()

# to apply context manager in class, we use enter n exit method

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
        print('exit')

with ManagedFile('notes.txt') as file:
    print('do some stuffffff....')
    file.write('soome todoooooooo....')