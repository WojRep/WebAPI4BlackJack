from flask_restful import Resource

class NoGame(Resource):
    def get(self):
        return {'status': 'OK'}

class PlayGame(Resource):
    def get(self, game_id, game_data=[]):
        pass

    def post(self, game_id, game_data=[]):
        pass

    def put(self, game_id, game_data=[]):
        pass

    def delete(self, game_id, game_data=[]):
        pass