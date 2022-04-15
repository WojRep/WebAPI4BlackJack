Intro to Flask-TESTful: [Flask-RESTful - How to quickly build API - Blog j-labs](https://blog.j-labs.pl/flask-restful)

###############################################
###############################################

GET:

    /game/new -> nowa gra, zwracamy game_id

        {
            game_id: guid
            }

        losowy GUID liczba określająca niepowtarzalny identyfikator gry, 32 znaki, hex






    /game/{GUID-GAME}

        {
            game_id: guid,
            game_status: status,
            deck: [],
            players: {

            }
        }

        game_id: losowy GUID liczba określająca niepowtarzalny identyfikator gry, 32 znaki, hex

        game_status:
            new -> nowa gra nie zainicjowana
            progress -> gra w trakcie


    /game/{GUID-GAME}/<command>

        command:

            getonecard -> Wydanie jednej karty graczowi
