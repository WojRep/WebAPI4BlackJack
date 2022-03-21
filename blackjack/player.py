class Player:
    """
    Definiujemy gracza
    """
    def __init__(self, name):
        self.cards_score = 0
        self.cards = []
        self.player_name = name

    def add_card(self, card):
        """
        Dodaje jedna kartę do kart gracza

        Args:
            card (int): zwracamy wartość karty
        """
        if card.card_value in ["Jack", "Queen", "King"]:
            self.cards_score += 10
        elif card.card_value == "Ace":
            if len(self.cards) > 2:
                self.cards_score += 1
            else:
                self.cards_score += 11
        else:
            self.cards_score += int(card.card_value)
        self.cards.append(card)
        return self.cards_score


    def show_cards(self):
        """Zwraca karty danego gracza.

        Returns:
            str: lista kart gracza
        """
        my_cards = ""
        my_cards = [ (my_cards + str(card)) for card in list(self.cards)]
        return my_cards

