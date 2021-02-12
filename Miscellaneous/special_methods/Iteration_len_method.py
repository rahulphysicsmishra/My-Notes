print(len([1, 2, 3, 4, 5]))  # length of list

print(len({"spades", "club", "diamond", "heart"}))  # length of set

print(len(("alpha", "beta", "gamma")))  # length of tuple

print(len({"mango": 10, "apple": 40, "plum": 16}))  # length of dictionary

#  len() function doesn't work with a generator.

def gen_func():
    for i in range(5):
        yield i

# print(len(gen_func()))  # Throwing type error, object of type generator has no len()


# len() with User defined objects by using __len__() method

class Stack:

    def __init__(self):
        self._stack = []

    def push(self, item):
        self._stack.append(item)

    def pop(self):
        self._stack.pop()

    def __len__(self):
        return len(self._stack)

s = Stack()
print("Length before push is: ", len(s))
s.push(2)
s.push(4)
s.push(5)
s.pop()
s.push(10)
print("Length after push and pop is :", len(s))



