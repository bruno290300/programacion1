from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import BolsonModel
import datetime as dt



class BolsonesPrevios(Resource):
    date = dt.datetime.today() - dt.timedelta(days=7)

    def get(self):
        page = 1
        per_page = 10

        bolsones = db.session.query(BolsonModel).filter(BolsonModel.fecha <= self.date)

        if request.get_json():
            filters = request.get_json().items()
            for key, value in filters:
                if key == 'page':
                    page = int(value)
                elif key == 'per_page':
                    per_page = int(value)

        bolsones = bolsones.paginate(page, per_page, True, 30)

        return jsonify({
            'bolsonesprevios': [bolson.to_json() for bolson in bolsones.items],
            'total': bolsones.total,
            'pages': bolsones.pages,
            'page': page
        })

class BolsonPrevio(Resource):
    def get(self, id):
        if int(id) in BOLSONESPREVIOS:
            return BOLSONESPREVIOS[int(id)]
        return "", 404