# Importujemy
import base
# Flask RESTful
api = base.Api(base.app)
from game_api import NoGame, PlayGame, PlayNewGame
api.add_resource(NoGame, '/')
api.add_resource(PlayNewGame,
                 '/game/new',
)
api.add_resource(PlayGame,
                 '/game/<game_id>',
                 '/game/<game_id>/',
                 '/game/<game_id>/<data>'
                 )
# głowny program
if __name__=="__main__":
    base.app.run(host='0.0.0.0',port='5050',debug=True)
