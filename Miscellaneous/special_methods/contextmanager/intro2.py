# Python program showing file management using context manager

class FileManager():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

# loading a file
with FileManager('test.txt', 'w') as f:
    f.write('Test')

print(f.closed)

# On executing the with block, the following operations happen in sequence:-
#1. A filemanager obj is created with test.txt as the filename
# and w(write) as a mode when __init__ method is executed.

#2. The __enter__ mehod opens the test.txt file in write mode(setup operations)
# and returns the filemanager object to variable f.

#3. The text 'Test' is written into the file.

#4. The __exit__ method takes care of closing the file on exiting with block(teardown process)
#   when print(f.closed) is run, the output is True as the filemanager
#   has already taken care of closing the file which otherwise
#  needed to be explicitly done.
