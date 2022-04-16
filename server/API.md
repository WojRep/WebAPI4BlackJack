Intro to Flask-TESTful: [Flask-RESTful - How to quickly build API - Blog j-labs](https://blog.j-labs.pl/flask-restful)

###############################################
###############################################

GET:

Rozpoczęcie nowej gry:
/game/new -> nowa gra, zwracamy game_id

        {
            game_id: guid
            }

        losowy GUID liczba określająca niepowtarzalny identyfikator gry, 32 znaki, hex

Pobranie stanu gry:
/game/{GUID-GAME}

        {
            game_id: guid,
            deck: [],
            players: {

            }
        }

        game_id: losowy GUID liczba określająca niepowtarzalny identyfikator gry, 32 znaki, hex

Prowadzenie gry:
/game/{GUID-GAME}/<command>

        command:

            getonecard -> Wydanie jednej karty graczowi

            willpass -> gracz pasuje, dalej gra krupier
