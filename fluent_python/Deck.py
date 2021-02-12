import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])  # returns a new subclass of tuple with named fields

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')  # it gives list of num from 2 to 11 and JQKA
    print(ranks)
    suits = 'spades diamonds clubs hearts'.split()
    print(suits)

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]  # gives list of card(rank,suit) wise for 52 cards
        print(self._cards)

    def __len__(self):
        return len(self._cards)  # gives length of deck

    def __getitem__(self, position):
        return self._cards[position]  # this is the method which provides deck[0], deck[1]... basically the position of the cards

beer_card = Card('7', 'diamonds')
print(beer_card)
deck = FrenchDeck()
print(len(deck), deck[0], deck[1])
print(choice(deck))
print(deck[:3])
print('*'*10)
print(deck[12::13])

# for card in deck:
#     print(card)
print(Card('J', 'spades') in deck)

print('*'*80)
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value*len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)
