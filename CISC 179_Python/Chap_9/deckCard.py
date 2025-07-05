import random

# The definition of the Card class goes here

class Deck(object):
    """ A deck containing 52 cards."""

    def __init__(self):
        """Creates a full deck of cards."""
        self.cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                c = Card(rank, suit)
                self.cards.append(c)

    def shuffle(self):
        """Shuffles the cards."""
        random.shuffle(self.cards)

    def deal(self):
        """Removes and returns the top card or None
        if the deck is empty."""
        if len(self) == 0:
            return None
        else:
            return self.cards.pop(0)

    def __len__(self):
        """Returns the number of cards left in the deck."""
        return len(self.cards)

    def __str__(self) :
        """Returns the string representation of a deck."""
        result = ""
        for c in self.cards:
            result = result + str(c) + '\n'
        return result
