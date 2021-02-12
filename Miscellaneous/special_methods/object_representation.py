"""To provide a string representation of your object
for the consumer of your class...

__repr__ -> The "official" string representation of an object.
             The goal of __repr__ is to be unambiguous.

__str__ -> The informal string representation of an object.

"""

class Account:
    def __init__(self, owner, amount = 0):
        self.owner = owner
        self.amount = amount
        self._transaction = []

    def __repr__(self):
        return 'Account({!r}, {!r})'.format(self.owner, self.amount)

    def __str__(self):
        return 'Account of {} with starting point: {}'.format(self.owner, self.amount)

acc = Account('john')
print(str(acc))
print(repr(acc))
print(acc)
