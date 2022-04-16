from card import *
from random import shuffle

class Deck:
    """
    Create decks of cards
    """
    def __init__(self):
        self.cards = []
        self.cards = [Card(color, value) for value in Card.posible_card_value for color in Card.posible_card_color]

    def issue_card(self):
        """
        Issue a card from a deck

        Returns:
            object: Card issued
        """
#        issued_card = self.cards[-1]
        issued_card = self.cards.pop()

        return issued_card

    def shuffle(self):
        """
        Shuffle the cards in the deck

        Returns:
            object: Shuffled Cards in the deck
        """
        return shuffle(self.cards)


