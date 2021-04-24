from flask_restful import Resource
from flask import request, jsonify




class BolsonesPrevios(Resource):
    def get(self):
        return BOLSONESPREVIOS


class BolsonPrevio(Resource):
    def get(self, id):
        if int(id) in BOLSONESPREVIOS:
            return BOLSONESPREVIOS[int(id)]
        return "", 404