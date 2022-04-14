from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

FUEL_CONSUMPTION = {
    '1': {'odometer': 0,
          'fuelQuantity': 0.0},
    '2': {'odometer': 100,
          'fuelQuantity': 12.5},
    '3': {'odometer': 300,
          'fuelQuantity': 30.0},
    '4': {'odometer': 400,
          'fuelQuantity': 8.5},
    '5': {'odometer': 500,
          'fuelQuantity': 9}
}


def abort_if_record_doesnt_exist(record_id):
    if record_id not in FUEL_CONSUMPTION:
        abort(404, message="Record {} doesn't exist".format(record_id))


class FuelConsumptionList(Resource):
    def get(self):
        return {"fuelConsumption": FUEL_CONSUMPTION}


class FuelConsumption(Resource):
    def get(self, record_id):
        abort_if_record_doesnt_exist(record_id)
        return FUEL_CONSUMPTION[record_id]


api.add_resource(FuelConsumptionList, '/recordList',
                                      '/')
api.add_resource(FuelConsumption, '/record/<record_id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5050',debug=True)