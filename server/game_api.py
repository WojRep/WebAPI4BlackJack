from flask_restful import Resource
from flask import jsonify
from game import Game
from deck import Deck
import jsonpickle
from game_exceptions import *

import base

#
# Dla przerzucania object -> json and from json -> object
#
from json import JSONEncoder

class ObjEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

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

        match data:
            case "getonecard":
                game =  jsonpickle.decode(q.game_data)

                if (game.players[0].cards_score >= 21) or (game.players[1].cards_score >= 21):
                    game_status="end"
                else:

                    game_status="getonecard"
                    new_card = game.deck.issue_card()
                    game.players[1].add_card(new_card)
                    if game.players[1].cards_score > 21:
                        game_status = "loser"
                    if game.players[1].cards_score == 21:
                        game_status = "winner"

                q.game_data = jsonpickle.encode(game)

                base.db.session.commit()

            case "willpass":
                game =  jsonpickle.decode(q.game_data)

                while True:
                    new_card = game.deck.issue_card()
                    game.players[0].add_card(new_card)
                    if game.players[0].cards_score > 21:
                        game_status = "Wygrałeś - krupier przekroczył 21 punkty"
                        break
                    if game.players[0].cards_score == 21:
                        game_status = "Przegrałeś - krupier ma 21 punkty"
                        break

            case "":
                game_status="Empty"


            case _:
                return {'game_status': 'ERROR on API'}

        q = base.db_game.query.filter_by(game_id=game_id).first()

        return {'game_id': game_id,
                'game_data': q.game_data,
                'game_status': game_status}

    def post(self, game_id, game_data=[]):
        pass

    def put(self, game_id, game_data=[]):
        pass

    def delete(self, game_id, game_data=[]):
        pass