from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import ClienteModel

#CLIENTES = {
    #1: {'firstname': 'Franco', 'lastname': 'Rosas'},
    #2: {'firstname': 'Yamila', 'lastname': 'Ramos'},
#}

class Clientes(Resource):
    
    def get(self):
        page = 1
        per_page = 10
        clientes = db.session.query(ClienteModel)
        if request.get_json():
            filters = request.get_json().items()
            for key, value in filters:
                if key =="page":
                    page = int(value)
                if key == "per_page":
                    per_page = int(value)
        clientes = clientes.paginate(page, per_page, True, 30)
        return jsonify({
                'clientes':[cliente.to_json() for cliente in clientes.items],
                'total': clientes.total,
                'pages': clientes.pages,
                'page': page

                })
                
            
                  

    def post(self):
        cliente = ClienteModel.from_json(request.get_json())
        db.session.add(cliente)
        db.session.commit()
        return cliente.to_json(), 201

class Cliente(Resource):
    """
    def get(self, id):
        if int(id) in CLIENTES:
            return CLIENTES[int(id)]
        return "", 404

    def delete(self, id):
        if int(id) in CLIENTES:
            del CLIENTES[int(id)]
            return '', 204
        return '', 404

    def put(self, id):
        if int(id) in CLIENTES:
            cliente = CLIENTES[int(id)]
            date = request.get_json()
            cliente.update(date)
            return cliente, 201
        return '', 404
    """
    def get(self, id):
        cliente = db.session.query(ClienteModel).get_or_404(id)
        return cliente.to_json()

    def delete(self, id):
        cliente = db.session.query(ClienteModel).get_or_404(id)
        db.session.delete(cliente)
        db.session.commit()
        return '', 204

    def put(self, id):
        cliente = db.session.query(ClienteModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(cliente, key, value)
        db.session.add(cliente)
        db.session.commit()
        return cliente.to_json(), 201