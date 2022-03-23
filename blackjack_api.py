"""rest api for black jack game"""

import errno
from flask import Flask, render_template, request, jsonify
import jsonpickle
from json import JSONEncoder
from blackjack.exception import *
from blackjack.blackjack import BlackJack

cards_folder = "statics/cards"
card_filename_prefix = "nicubunu_Ornamental_deck_"

api = Flask(__name__)
api.config['SECRET_KEY'] = 'dsdsdsdsdsd'

@api.route('/', methods=['GET'])
def welcame():
    """handling of GET request """
    game_state = 'Start'
    game_id = 'test_id'
    return jsonify({
        'game_state': game_state,
        'game_id' : game_id
        })

@api.route('/', methods=['POST'])
def game():
    """handling of POST requests """
    if request.is_json:
        response = request.get_json()
        game_state = response['game_state']
        game_id = response['game_id']

    if game_id == 'test_id':
        if game_state == 'GetOneCard':
            return jsonify({'game_state' : game_state})
        elif game_state == 'WillPass':
            return jsonify({'game_state' : game_state})
        else:
            raise GameError('Unexpected Error')
    else:
        return jsonify({'game_state': 'error'})

if __name__ == '__main__':
    api.run()
