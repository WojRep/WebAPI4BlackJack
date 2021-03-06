"""logic of the game"""

from this import s
from blackjack.exception import GameWinner, GameError, GameOver
from blackjack.blackjack import BlackJack

GAME_DICT = {'game_id' : None, 'deck' : None, 'croupier_cards' : None, 'player_cards' : None}

class IdAlreadyExist(Exception):
    """exception when new user called game in use"""

class Game:
    """initialization and game methods

    Raises:
        IdAlreadyExist: exception when new user called game in use
        GameWinner: exception when any player 21 scored
        GameLoser: exception when any player above 21
    """
    games_list = []

    def __init__(self, game_id) -> None:
        self.game_id = game_id
        self.check_id()
        self.game = BlackJack(self.game_id)

    @staticmethod
    def call_game(game_id = None, method = None, filed = None):
        """A static method calling the appropriate game instance according to the ID

        Args:
            game_id (game_id): the user's game ID
            method (str): the name of the called class method
            filed (str): the name of the called class filed

        Returns:
            any, optional : instance field if called
        """
        for game in Game.games_list:
            print(f'{game} --> {game.game_id} // ', end='')
        user_game = [game for game in Game.games_list if game.game_id == game_id]
        print(f'{user_game} --> {game_id}')
        if user_game:
            try:
                if method:
                    return getattr(user_game[0], method)()

                if filed:
                    return getattr(user_game[0], filed)

            except AttributeError as err:
                raise err
        else:
            raise GameError('unknown game id')

        return None

    def check_id(self):
        """Add game to list if not exist"""
        if self.game_id not in [game.game_id for game in Game.games_list]:
            Game.games_list.append(self)
        else:
            raise IdAlreadyExist('game id is busy')

    def start_game(self):
        """the first hand in the game

        Returns:
            list[Card], list[Card], Exception: stored card by croupier,
            stored card by user, game exception
        """
        err = None
        self.game.get_deck()
        self.game.create_players()
        self.game.deal_cards(2)
        if self.game.players[1].cards_score == 21:
            err = GameWinner(f'{self.game.players[1].player_name} zdoby?? 21. Wygrywa.')
        return self.game.players[0].cards[:], self.game.players[1].cards[:], err

    def get_one_card(self):
        """the player draws a card

        Returns:
            list[card], Exception: stored card by user, game exception
        """
        err = None
        new_card = self.game.issue_card()
        self.game.players[1].add_card(new_card)
        if self.game.players[1].cards_score > 21:
            err = GameOver(f'{self.game.players[1].player_name} przekroczy?? 21. Przegrywa.')
        return self.game.players[0].cards[:], self.game.players[1].cards[:], err

    def will_pass(self):
        """croupier turn

        Returns:
            list[card], Exception: stored card by croupier, game exception
        """
        err = None
        if self.game.players[0].cards_score == 21:
            err = GameOver(f'{self.game.players[0].player_name} zdoby?? 21. Wygrywa.')
        while self.game.players[0].cards_score < 17:
            new_card = self.game.issue_card()
            self.game.players[0].add_card(new_card)
        if self.game.players[0].cards_score > 21:
            err = GameWinner(f'{self.game.players[0].player_name} przekroczy?? 21. Przegrywa.')
        elif self.game.players[0].cards_score > self.game.players[1].cards_score:
            err = GameOver(f'{self.game.players[0].player_name} ma wi??cej punkt??w. Wygrywa')
        else:
            err = GameWinner(f'{self.game.players[1].player_name} ma wi??cej punkt??w. Wygrywa')
        return self.game.players[0].cards[:], self.game.players[1].cards[:], err

    def __del__(self):
        GAME_DICT['game_id'] = self.game_id
        GAME_DICT['croupier_cards'] = [str(card) for card in self.game.players[0].cards[:]]
        GAME_DICT['player_cards'] = [str(card) for card in self.game.players[1].cards[:]]
        GAME_DICT['deck'] = [str(card) for card in self.game.my_deck[:]]

        print(GAME_DICT)
