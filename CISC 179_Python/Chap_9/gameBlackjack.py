from blackjack import Blackjack
game = Blackjack()
game.play()

class Dealer(Player) :
    """Like a Player, but with some restrictions."""

    def __init__(self, cards):
        """Initial state: show one card only."""
        Player.__init__(self, cards)
        self.showOneCard = True

    def __str__(self) :
        """Return just one card if not hit yet."""
        if self.showOneCard:
            return str(self.cards[0])
        else:
            return Player.__str__(self)

    def hit(self, deck):
        """Add cards while points < 17,
        then allow all to be shown."""
        self.showOneCard = False
        while self.getPoints() < 17:
            self.cards.append(deck.deal())
