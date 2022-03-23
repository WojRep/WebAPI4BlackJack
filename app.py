from flask import Flask, render_template, send_from_directory, request, redirect, url_for, session
from os import listdir
from os.path import isfile, join
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
        game_state = "Start"
        return render_template("index.html", game_state = game_state)
    elif (request.method == 'POST'):
        try:
            if (request.form.get('startgame') == "StartGame"):
                game_state = "playing"
                game = BlackJack()
                game.get_deck()
                game.create_players()
                #game_debug = game.my_deck
                game.deal_cards(2)

            elif (request.form.get('getonecard') == "GetOneCard"):
                game_session = session.get('game')
                game = jsonpickle.decode(game_session)
                new_card = game.issue_card()
                game.players[1].add_card(new_card)

            elif (request.form.get('willpass') == "WillPass"):
                game_session = session.get('game')
                game = jsonpickle.decode(game_session)
                while True:
                    new_card = game.issue_card()
                    game.players[0].add_card(new_card)
                    if game.players[0].cards_score > 21:
                        raise GameWinner("Wygrałeś - krupier przekroczył 21 punkty")
                    if game.players[0].cards_score == 21:
                        raise GameOver("Przegrałeś - krupier ma 21 punkty")
            else:
                raise GameError("Unexpected Error")
            if (game.players[1].cards_score == 21) and (game.players[0].cards_score < 21):
                raise GameWinner("Wygrałeś, masz 21 punktu")
            elif (game.players[1].cards_score > 21) or \
                ((game.players[1].cards_score < 21) and (game.players[0].cards_score == 21)):
                raise GameOver("Przegrałeś - przekroczono 21 punkty")
            elif ((game).players[1].cards_score == 21) and (game.players[0].cards_score == 21):
                raise GameToDraw("Remis")
            elif (game.players[1].cards_score < 21) and (game.players[0].cards_score < 21):
                game_state = "playing"

        except GameOver:
            game_state = "ToMany"

        except GameWinner:
            game_state = "Winner"

        except GameLoser:
            game_state = "Loser"

        except GameToDraw:
            game_state = "ToDraw"

        except GameError:
            game_state = "GameError"

        except:
            game_state = "Totalnie coś poszło nie tak !!!"
            return render_template("index.html", game_state = game_state)


        finally:
            session['game'] = jsonpickle.encode(game)
            #game_debug = session.get('game')
            croupier_cards = game.show_cards(0)[1]
            if len(croupier_cards) == 2 and game_state == 'playing':
                croupier_cards[1] = 'reverse.png'
            croupier_score = game.show_cards(0)[0]
            player_cards = game.show_cards(1)[1]
            player_score = game.show_cards(1)[0]
            return render_template("play-game.html", \
                cards_folder = cards_folder, \
                croupier_cards = croupier_cards, croupier_score = croupier_score, \
                player_cards = player_cards, player_score = player_score, game_state = game_state, game_debug = game_debug)

    else:
        game_state = "inne"
        return render_template("index.html", game_state = game_state, game_debug = game_debug)

if __name__=="__main__":
#    app.run(flask_config)
    app.run()