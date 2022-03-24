"""logic of the game"""

from blackjack.exception import *
from blackjack.blackjack import BlackJack

class IdAlreadyExist(Exception):
    """_summary_
    """

class Game:
    """_summary_
    """
    games_list : list[BlackJack] = []
    def __init__(self, game_id) -> None:
        self.game_id = game_id

    def check_id(self):
        """Add game_id to list if not exist"""
        if self.game_id not in Game.games_list:
            self.game_id = BlackJack(self.game_id)
            Game.games_list.append(self.game_id)
        else:
            raise IdAlreadyExist('game is busy')

    def start_game(self):
        game = BlackJack()
        game.get_deck()
        game.create_players()
        game.deal_cards(2)