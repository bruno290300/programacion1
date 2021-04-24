from flask_restful import Resource
from flask import request, jsonify



class BolsonesVenta(Resource):
    def get(self):
        return BOLSONESVENTA


class BolsonVenta(Resource):
    def get(self, id):
        if int(id) in BOLSONESVENTA:
            return BOLSONESVENTA[int(id)]
        return "", 404