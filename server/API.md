Intro to Flask-TESTful: [Flask-RESTful - How to quickly build API - Blog j-labs](https://blog.j-labs.pl/flask-restful)

###############################################
###############################################

GET:

/game/new -> nowa gra, zwracamy game_id, game_status

    game_id: losowy GUID liczba określająca niepowtarzalny identyfikator gry, 32 znaki, hex

    game_status:
        new -> nowa gra nie zainicjowana
        progress -> gra w trakcie

POST:
/game/
