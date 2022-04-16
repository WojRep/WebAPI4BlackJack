from deck import *

class Player:
    """
    Definiujemy gracza
    """
    def __init__(self, name):
        self.player_name = name
        self.cards_score = 0
        self.cards = []


    def add_card(self, card):
        """
        Dodaje jedna kartę do kart gracza

        Args:
            card (int): zwracamy wartość karty
        """
        self.cards.append(card)
        # calculate score of card
        if card.card_value in ["J", "Q", "K"]:
            self.cards_score += 10
        elif card.card_value == "A":
            number_of_aces = len([card for card in self.cards if card.card_value == "A"])
            if (number_of_aces == 1 and len(self.cards) == 2):
                self.cards_score += 10
            elif (number_of_aces == 1 and len(self.cards) > 2):
                self.cards_score += 1
            elif ((len(self.cards) > 2) and (self.cards_score > (21 - 11))):
                self.cards_score += 1
            else:
                self.cards_score += 11
        else:
            self.cards_score += int(card.card_value)

        return self.cards_score

    def _repr__(self):
        player_cards =[]
        return [self.player_name, self.cards_score, [player_cards.append(str(card)) for card in list(self.cards)]]


    # def show_cards(self):
    #     """Zwraca karty danego gracza.

    #     Returns:
    #         str: lista kart gracza
    #     """
    #     my_cards = ""
    #     # for card in list(self.cards):
    #     #     my_cards = my_cards + str(card) + ", "
    #     my_cards = [ (my_cards + str(card) + ", ") for card in list(self.cards)]
    #     return my_cards
