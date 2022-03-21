from random import shuffle

class Card:
    """
    Definiujemy kartę do gry
    """
    def __init__(self, card_color, card_value):
        # TODO: Przekazywanie szablony nazwy pliku z kartami
        card_filename_prefix = "nicubunu_Ornamental_deck_"
        #
        self.card_color = card_color
        self.card_value = card_value
        self.name = card_filename_prefix + card_value + "_of_" + card_color +".png"

    def __str__(self):
        return self.name


class Deck:
    """
    Tworzymy talie kart
    """
    def __init__(self):
        self.deck = []


    def __len__(self):
        return len(self.deck)

    def create_deck(self):
        # Tworzymy talie kart
        self.cards = []
        card_color = ["clubs", "diamonds", "hearts", "spades"]
        card_value = ["2", "3", "4", "5", "6", "7", "8", "9", "10", \
            "Jack", "Queen", "King", "Ace"]
        self.deck = [Card(color, value) for value in card_value for color in card_color]


    def shuffle(self):
        """
        Tasuje karty w talii

        Returns:
            object: potasowane karty
        """
        return shuffle(self.deck)

    def show(self):
        """
        Zwraca nazwy plików kart w talii

        Returns:
            _type_: _description_
        """
        cards_list =[]

        for _ in enumerate(self.deck):
            cards_list.append(self.deck[_[0]].name)
        return cards_list
