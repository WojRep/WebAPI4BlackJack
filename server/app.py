from flask import Flask, jsonify, request, redirect, session

from flask_restful import Resource, Api

from game_api import NoGame, PlayGame

app=Flask(__name__)
api = Api(app)




api.add_resource(NoGame, '/game',
                         '/game/',
                         '/')

api.add_resource(PlayGame, '/game/<game_id>/',
                           '/game/<game_id>/<game_data>')



if __name__=="__main__":
    app.run(host='0.0.0.0',port='5050',debug=True)
