class InvalidCardColor(Exception):
    pass

class InvalidCardValue(Exception):
    pass


class Card:
    """
    Define a playing card

    H - hearts
    D - diamonds
    C - clubs
    S - spades

    J - Jack
    Q - Queen
    K - King
    A - Ace
    """
    posible_card_color = ["H", "D", "C", "S"]
    posible_card_value = ["2", "3", "4", "5", "6", "7", "8", "9", "10", \
        "J", "Q", "K", "A"]

    def __init__(self, card_color, card_value):
        if card_color not in self.posible_card_color:
            raise InvalidCardColor('Invalid color of card.')

        self.card_color = card_color

        if card_value not in self.posible_card_value:
            raise InvalidCardValue('Invalid value of card.')

        self.card_value = card_value

        # self.name = card_value + card_color

    def __repr__(self):
        return f'{self.card_value}:{self.card_color}'