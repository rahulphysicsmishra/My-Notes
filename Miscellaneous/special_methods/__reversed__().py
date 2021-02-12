"""The reversed() function allows us to process the items
in a sequence in reverse order. It accepts a sequence and returns
an iterator."""

print(reversed([44, 11, -90, 55, 3]))

print(list(reversed([44, 11, -90, 55, 3])))  # reversing a list

print(list(reversed((6, 1, 3, 9))))  # reversing a tuple

print(list(reversed("Hello")))  # reversing a string

# The argument passed to reversed() must be a proper
# sequence. Trying to pass objects which do not maintain
# their orders like dict and set will result in a type error.

#print(reversed({0, 4, -2, 12, 6}))  # type error: set object is not reversible


# Reversing User-defined objects
# To reverse user-defined objects the class must do one of the following:

#1. Implement __len__() and __getitem__() methods; or
#2. Implement __reversed__() method

from collections import namedtuple

Card = namedtuple('Card', ['rank', 'suit'])

class CardDeck:
    suits = ('club', 'diamond', 'heart', 'spades')
    ranks = tuple((str(i) for i in range(2, 11))) + tuple("JQKA")

    def __init__(self):
        self._cards = [Card(r, s) for s in self.suits for r in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, index):
        return self._cards[index]

    # def __reversed__(self):  this is for reversed method
    #    return self._cards[::-1]


deck = CardDeck()
print(deck)
print(deck[0], deck[1])
reversed_deck = list(reversed(deck))
print(reversed_deck[0], reversed_deck[-1])


