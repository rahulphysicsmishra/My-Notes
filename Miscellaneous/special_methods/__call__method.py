"""The __call__() method enables python programmers to write
classes where the instances behave like functions and can be
called like a function.
"""

class Example:
    def __init__(self):
        print("Instance created")

    # defining call method
    def __call__(self, a, b):
        print("Instance is called via special method")
        print(a * b)

ans = Example()  # Instance created
ans(10, 20)  # __call__ method will be called
