"""rest api for black jack game"""

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
    game_state = 'Start'
    game_id = 'test_id'
    return jsonify(game_state, game_id)

if __name__ == '__main__':
    api.run()
