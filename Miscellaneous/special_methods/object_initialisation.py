""" A class may define a special method named __init__(), like this

def __init__(self):
    self.data = []"""

class Account:
    """A simple account class"""

    def __init__(self, owner, amount = 0):
        self.owner = owner
        self.amount = amount
        self._transaction = []

# The constructor takes care of setting up the object
# In this case it receives the owner name, an optional
# start amount and defines an internal transactions
# list to keep track of deposits and withdrawals.
acc = Account('bob')
acc.amount = 40
print(acc.amount)

# Another example
class Complex():
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r, x.i)
