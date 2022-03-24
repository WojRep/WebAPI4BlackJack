from flask import Flask, render_template, send_from_directory, request, redirect, url_for, session
from os import listdir
from os.path import isfile, join
from random import choice
#
import json
import jsonpickle
from json import JSONEncoder
#

#
# folder z kartami
cards_folder = "statics/cards"
card_filename_prefix = "nicubunu_Ornamental_deck_"
#

# from blackjack.deck import *
# from blackjack.player import *
from blackjack.exception import *
from blackjack.blackjack import BlackJack
from blackjack.game import Game





"""
Dokumentacja CONFIG Flask => https://flask.palletsprojects.com/en/1.0.x/config/
"""
flask_config = {
    "DEBUG": True,	# Włącza debugowanie => automatyczny reload zmiany strony
    "TESTING": False,
#    "TEMPLATES_AUTO_RELOAD": True,
}

app=Flask(__name__)
app.config['SECRET_KEY'] = 'dsdsdsdsdsd'


class ObjEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


@app.route('/statics/<path:path>')
def fonts(path):
    """
    It allows you to display and download all static files from the /static/ folder.
    """
    return send_from_directory('statics', path)

@app.route('/',methods = ['POST', 'GET'])
def index():
    game_state = "INIT_START"
    game_debug = ""
    if (request.method == 'GET'):
        game_id = 'test_app_id' + choice(['a','b','c','d'])
        game_state = "Start"
        Game(game_id)
        return render_template("index.html", game_state = game_state, game_id = game_id)
    elif (request.method == 'POST'):
        try:
            if (request.form.get('startgame') == "StartGame"):
                game_id = request.form.get('game_id')
                croupier_cards, player_cards, err = Game.call_game(game_id, method = 'start_game')
                if err:
                    raise err

            elif (request.form.get('getonecard') == "GetOneCard"):
                game_id = request.form.get('game_id')
                croupier_cards, player_cards, err = Game.call_game(game_id, method = 'get_one_card')
                if err:
                    raise err

            elif (request.form.get('willpass') == "WillPass"):
                game_id = request.form.get('game_id')
                croupier_cards, player_cards, err = Game.call_game(game_id, method = 'will_pass')
                if err:
                    raise err

        except GameOver:
            game_state = "ToMany"

        except GameWinner as winner:
            game_state = winner

        except GameLoser as loser:
            game_state = loser

        except GameToDraw:
            game_state = "ToDraw"

        except GameError:
            game_state = "GameError"

        except:
            game_state = "Totalnie coś poszło nie tak !!!"
            return render_template("index.html", game_state = game_state)


        finally:
            #session['game'] = jsonpickle.encode(game)
            #game_debug = session.get('game')
            #croupier_cards = game.show_cards(0)[1]
            if croupier_cards and len(croupier_cards) == 2 and game_state == 'playing':
                croupier_cards[1] = 'reverse.png'
            croupier_score = Game.call_game(game_id, filed = 'game').players[0].cards_score
            #player_cards = game.show_cards(1)[1]
            player_score = Game.call_game(game_id, filed = 'game').players[1].cards_score
            return render_template("play-game.html", \
                cards_folder = cards_folder, game_id = game_id,\
                croupier_cards = croupier_cards, croupier_score = croupier_score, \
                player_cards = player_cards, player_score = player_score, game_state = game_state, game_debug = game_debug)

    else:
        game_state = "inne"
        return render_template("index.html", game_state = game_state, game_debug = game_debug)

if __name__=="__main__":
#    app.run(flask_config)
    app.run()