from ast import Break
from tkinter.messagebox import RETRY
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
from blackjack.game import call_game





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

@app.route('/', methods = ['GET'])
def index():
    game_state = "INIT_START"
    game_debug = ""
    session.clear()

    game_id = call_game(method='generate_new_id')
    game_state = "Start"
    session['game_id'] = game_id
    return render_template("index.html", game_state = game_state)

@app.route('/', methods = ['POST'])
def play_game():
    if 'game_id' in session:
        game_id = session['game_id']
        game_state = "playing"
        winner_msg = None
        croupier_cards = None
        try:
            if (request.form.get('startgame') == "StartGame"):
                croupier_cards, player_cards, err = call_game(game_id, method = 'start_game')
                if err:
                    raise err

            elif (request.form.get('getonecard') == "GetOneCard"):
                croupier_cards, player_cards, err = call_game(game_id, method = 'get_one_card')
                if err:
                    raise err

            elif (request.form.get('willpass') == "WillPass"):
                croupier_cards, player_cards, err = call_game(game_id, method = 'will_pass')
                if err:
                    raise err
            else:
                raise GameError('unknown game state')

        except GameOver as msg:
            winner_msg = msg
            game_state = "ToMany"

        except GameWinner as msg:
            winner_msg = msg
            game_state = "Winner"

        except GameLoser as msg:
            winner_msg = msg
            game_state = "Loser"

        except GameToDraw as msg:
            winner_msg = msg
            game_state = "ToDraw"

        except GameError as msg:
            winner_msg = msg
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
            croupier_score = 0 #Game.call_game(game_id, filed = 'game').players[0].cards_score
            #player_cards = game.show_cards(1)[1]
            player_score = 0 #Game.call_game(game_id, filed = 'game').players[1].cards_score
            return render_template("play-game.html", \
                cards_folder = cards_folder,\
                croupier_cards = croupier_cards, croupier_score = croupier_score, \
                player_cards = player_cards, player_score = player_score, game_state = game_state, winner_message = winner_msg)

    else:
        game_state = "inne"
        return redirect(url_for('index'))

if __name__=="__main__":
#    app.run(flask_config)
    app.run()
