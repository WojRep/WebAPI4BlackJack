import uuid

from flask import jsonify
from player import Player
from deck import Deck
import json

class Game(object):
    """
    Klasa od prowadzenia gry
    """
    def __init__(self, *args, **kwargs):
        """
        Tworzymy grę z graczami

        Args:
            players (int): Ilość graczy
        """
        self.players = []
        self.deck = []
        self.guid = uuid.uuid4().hex

    def new_player(self, name):
        self.players.append(Player(name))

    def deal_cards(self, numbers_of_cards):
        """
        Rozdajemy karty
        """
        for  player_number in range(len(self.players)-1, -1, -1):
            for _ in range(numbers_of_cards):
                self.players[player_number].add_card(self.deck.issue_card())

    def new_game(self, players_name = ["Player1"]):
        """ Tworzymy nową grę """
        # Tworzymy graczy
        self.new_player("Croupier")
        for player in players_name:
            self.new_player(player)
        # Tworzymy talie kart
        self.deck = Deck()
        # Tasujemy karty
        self.deck.shuffle()
        # Wydajemy graczom po 2 karty
        self.deal_cards(2)

    def __repr__(self):
        guid = self.guid
        deck = str(self.deck)
        players = {}
        players.update({str(self.players[n].player_name): {'cards': self.players[n].cards.__str__(), 'score': self.players[n].cards_score} for n in range(len(self.players) )})
        data = {'game_id': guid, 'deck': deck, 'players': players}
        return data




