"""logic of the game"""

from blackjack.exception import GameWinner, GameError, GameOver
from blackjack.blackjack import BlackJack
from blackjack.deck import Card

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

    def __init__(self, game_id) -> None:
        self.game_id = game_id
        self.curent_game = BlackJack(self.game_id)
        self.curent_game.create_players()
        self.croupier = self.curent_game.players[0]
        self.user = self.curent_game.players[1]



    @staticmethod
    def generate_new_id():
        new_id = 'test'
        return new_id

    def restore_cards(self, cards_ovner, cards_list):
        for card in cards_list:
            cards_ovner.add_card(Card.create_card_from_name(card))

    def start_game(self):
        """the first hand in the game

        Returns:
            list[Card], list[Card], Exception: stored card by croupier,
            stored card by user, game exception
        """
        err = None
        self.curent_game.get_deck()
        self.curent_game.deal_cards(2)

        if self.user.cards_score == 21:
            err = GameWinner(f'{self.user.player_name} zdobył 21. Wygrywa.')
        return {
            'croupier_cards' : self.croupier.cards[:],
            'croupier_score' : self.croupier.cards_score,
            'user_cards' : self.user.cards[:],
            'user_score' : self.user.cards_score,
            'exception' : err
        }

    def get_one_card(self, deck, croupier_cards, player_cards):
        """the player draws a card

        Returns:
            list[card], Exception: stored card by user, game exception
        """
        err = None
        self.curent_game.my_deck = [Card.create_card_from_name(card) for card in deck]

        self.restore_cards(self.croupier, croupier_cards)
        self.restore_cards(self.user, player_cards)

        new_card = self.curent_game.issue_card()
        self.user.add_card(new_card)
        if self.user.cards_score > 21:
            err = GameOver(f'{self.user.player_name} przekroczył 21. Przegrywa.')
        return {
            'croupier_cards' : self.croupier.cards[:],
            'croupier_score' : self.croupier.cards_score,
            'user_cards' : self.user.cards[:],
            'user_score' : self.user.cards_score,
            'exception' : err
        }

    def will_pass(self, deck, croupier_cards, player_cards):
        """croupier turn

        Returns:
            list[card], Exception: stored card by croupier, game exception
        """
        err = None
        self.curent_game.my_deck = [Card.create_card_from_name(card) for card in deck]

        self.restore_cards(self.croupier, croupier_cards)
        self.restore_cards(self.user, player_cards)

        if self.croupier.cards_score == 21:
            err = GameOver(f'{self.croupier.player_name} zdobył 21. Wygrywa.')
        while self.croupier.cards_score < 17:
            new_card = self.curent_game.issue_card()
            self.croupier.add_card(new_card)
        if self.croupier.cards_score > 21:
            err = GameWinner(f'{self.croupier.player_name} przekroczył 21. Przegrywa.')
        elif self.croupier.cards_score > self.user.cards_score:
            err = GameOver(f'{self.croupier.player_name} ma więcej punktów. Wygrywa')
        else:
            err = GameWinner(f'{self.user.player_name} ma więcej punktów. Wygrywa')
        return {
            'croupier_cards' : self.croupier.cards[:],
            'croupier_score' : self.croupier.cards_score,
            'user_cards' : self.user.cards[:],
            'user_score' : self.user.cards_score,
            'exception' : err
        }

    def __del__(self):
        GAME_DICT['game_id'] = self.game_id
        GAME_DICT['croupier_cards'] = [str(card) for card in self.croupier.cards[:]]
        GAME_DICT['player_cards'] = [str(card) for card in self.user.cards[:]]
        GAME_DICT['deck'] = [str(card) for card in self.curent_game.my_deck[:]]



def call_game(game_id = None, method = None):
    """function calling the appropriate game instance according to the ID

    Args:
        game_id (game_id): the user's game ID
        method (str): the name of the called class method

    Returns:
        any, optional : instance field if called
    """
    if not game_id:
        return getattr(Game, 'generate_new_id')()

    if method == 'start_game':
        return getattr(Game(game_id), 'start_game')()

    if game_id == GAME_DICT['game_id'] and method:
        try:
            return getattr(Game(game_id), method)(deck = GAME_DICT['deck'],
                croupier_cards = GAME_DICT['croupier_cards'],
                player_cards = GAME_DICT['player_cards'])

        except AttributeError as err:
            raise err
    else:
        return None