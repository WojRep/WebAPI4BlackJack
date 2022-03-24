from blackjack.deck import *
from blackjack.player import *
from blackjack.exception import GameOver, GameWinner as Winner

class BlackJack(object):
    """
    Klasa od prowadzenia gry
    """
    def __init__(self, name, *args, **kwargs):
        """
        Tworzymy grę z graczami

        Args:
            players (int): Ilość graczy
        """
        self.players = []
        self.my_deck = []
        self.name = name

    def create_players(self):
        #Tworzymy podana ilość graczy.
        #Zakładamy,ze gracz [0] jest krupierem
        self.players = [Player(number_player) for number_player in range(2)]

    def get_deck(self):
        deck = Deck()
        deck.create_deck()
        deck.shuffle()
        self.my_deck = deck.deck

    def deal_cards(self, numbers_of_cards):
        """
        Rozdajemy karty
        """
        for  player_number in range(len(self.players)-1, -1, -1):
            for _ in range(numbers_of_cards):
                self.players[player_number].add_card(self.issue_card())


    def show_cards(self, player_number):
        """
        Zwracamy karty i punkty gracza
        """
        cards = [self.players[player_number].cards_score, self.players[player_number].show_cards()]
        return cards

    def issue_card(self):
        return_deck = self.my_deck[-1]
        self.my_deck = self.my_deck[:-1]
        return return_deck

    def play_again(self):
        """
        Gramy dalej.
        Pobieramy kolejna kartę.

        Raises:
            Winner: Wygraliśmy
            GameOver: Kiedy przegraliśmy
        """
        if (self.players[1].cards_score == 21) and (self.players[0].cards_score < 21):
            raise Winner("Wygrałeś, masz 21 punktu")

        while True:
            self.show_cards()
            key = input("Graczu, czy chcesz dobrać kartę (t/n): ")
            if key == "t":
                new_card = self.issue_card()
                print()
                print(f"Dostałeś kartę: {new_card}")
                print()
                self.players[1].add_card(new_card)

                if self.players[1].cards_score > 21:
                    print(f"Przekroczyłeś 21 punktów, masz: {self.players[1].cards_score}")
                    raise GameOver("Przegrałeś - przekroczono 21 punkty")
                if self.players[1].cards_score == 21:
                    raise Winner("Wygrałeś, masz 21 punktu")
            elif key == "n":
                if self.players[1].cards_score >= self.players[0].cards_score:
                    self.croupier()
                else:
                    raise GameOver("Przegrałeś - krupier ma więcej punktow")
            else:
                print("Nacisnąłeś niepoprawny klawisz")

    def croupier(self):
        """
        Krupier gra dalej ...

        Raises:
            Winner: Wygrales
            GameOver: Przegrales
        """
        while True:
            new_card = self.deck.issue_card()
            self.players[0].add_card(new_card)
            if self.players[0].cards_score > 21:
                print(f"Krupier przekroczył 21 punktów, ma: {self.players[0].cards_score}")
                raise Winner("Wygrałeś - krupier przekroczył 21 punkty")
            if self.players[0].cards_score == 21:
                raise GameOver("Przegrałeś - krupier ma 21 punkty")


    def __len__(self):
        """
        Podaje ilość graczy

        Returns:
            int:ść graczy
        """
        return len(self.players)
