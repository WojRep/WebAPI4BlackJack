from flask_restful import Resource
from flask import jsonify
from game import Game
from deck import Deck
import jsonpickle
from game_exceptions import *
import base

# #
# # Dla przerzucania object -> json and from json -> object
# #
# from json import JSONEncoder

# class ObjEncoder(JSONEncoder):
#     def default(self, o):
#         return o.__dict__

class NoGame(Resource):
    def get(self):
        return {'status': 'OK'}

class PlayNewGame(Resource):
    def get(self):
        game = Game()
        game.new_game()
        #
        # Zapis do bazy danych zainicjowanej gry
        game_id = game.guid
        # exportujemy obiekty do formatu json
        game_data = jsonpickle.encode(game)
        # wysyłamy do bazy
        query = base.db_game(game_id, game_data)
        base.db.session.add(query)
        base.db.session.commit()
        return {'game_id': game.guid}

class PlayGame(Resource):
    def get(self, game_id, data=""):
        game_status="__None___"

        q = base.db_game.query.filter_by(game_id=game_id).first()
        game =  jsonpickle.decode(q.game_data)
        match data:
            case "getonecard":
                # Jeśli punkty są >= 21 to nie pobiera nowej karty
                if not ((game.players[0].cards_score >= 21) or (game.players[1].cards_score >= 21)):
                    new_card = game.deck.issue_card()
                    game.players[1].add_card(new_card)
                    if game.players[1].cards_score > 21:
                        game_status = "loser"
                    if game.players[1].cards_score == 21:
                        game_status = "winner"
                    # Zapisujamy zmiany do bazy
                    q.game_data = jsonpickle.encode(game)
                    base.db.session.commit()
            case "willpass":
                while True:
                    new_card = game.deck.issue_card()
                    game.players[0].add_card(new_card)
                    q.game_data = jsonpickle.encode(game)
                    base.db.session.commit()
                    # Przerywa pobieranie kart dla krupiera jeśli osiągnie lub przekroczy 21 punty
                    if (game.players[0].cards_score > 21) or (game.players[0].cards_score == 21):
                        break
            case "":
                pass
            case _:
                return {'game_status': 'ERROR on API'}

        return game.__repr__()

    def post(self, game_id, game_data=[]):
        pass

    def put(self, game_id, game_data=[]):
        pass

    def delete(self, game_id, game_data=[]):
        pass