threeOfSpades = Card(3, "Spades")
jackOfSpades = Card(11, "Spades")
print(jackOfSpades)
threeOfSpades.rank < jackOfSpades.rank
print(jackOfSpades.rank, jackOfSpades.suit)

class Card(object):
    """ A card object with a suit and rank."""

    RANKS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
    SUITS = ("Spades", "Diamonds", "Hearts", "Clubs")

    def __init__(self, rank, suit):
        """Creates a card with the given rank and suit."""
        self.rank = rank
        self.suit = suit

    def __str__(self) :
        """Returns the string representation of a card."""
        if self.rank == 1:
            rank = "Ace"
        elif self.rank == 11:
            rank = "Jack"
        elif self.rank == 12:
            rank = "Queen"
        elif self.rank == 13:
            rank = "King"
        else:
            rank = self.rank
        return str(rank) + " of " + self.suit.

deck = Deck()
print(deck)
deck.shuffle()
len(deck)
while len(deck) > 0:
    card = deck.deal()
    print(card)
len(deck)


