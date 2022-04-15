from flask import Flask, jsonify, request, redirect, session

from flask_restful import Resource, Api
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///game.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicjalizacja struktury obiektu bazy poprzez FLASK w SQLAlchemy

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

# DB start init
class db_game(db.Model):
    """
    Tworzymy strukturę bazy danych
    table: db_game

    columns:
        game_id -> string -> przechowuje guid
        game_data -> text -> przechowuje grę
    """
    game_id = db.Column(db.String, nullable=False, primary_key=True)
    game_data = db.Column(db.Text)

    def __init__(self, game_id, game_data=[]):
        self.game_id = game_id
        self.game_data = game_data


#
# UWAGA: Plik bazy danych tworzy się TYLKO w czasie starty app.py (FLASK)
#
db.create_all() # Tworzy zdefiniowaną strukturę tabel



