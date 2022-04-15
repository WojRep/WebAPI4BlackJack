from base import db, db_game

id = '0d694b12c2c343e79bebfcbe51d616a7'

print(id)
result = db_game.query.filter_by(game_id=id).first()

print(result.game_id)