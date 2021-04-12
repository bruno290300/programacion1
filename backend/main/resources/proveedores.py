from flask_restful import Resource
from flask import request

PROVEEDORES = {
    1: {'firstname': 'cuyito', 'lastname': 'srl'},
    2: {'firstname': 'mendoagro', 'lastname': 'sa'},
}


class Proveedores(Resource):
    def get(self):
        return PROVEEDORES

    def post(self):
        proveedor = request.get_json()
        id = int(max(PROVEEDORES.keys())) + 1
        PROVEEDORES[id] = proveedor
        return PROVEEDORES[id], 201


class Proveedor(Resource):
    def get(self, id):
        if int(id) in PROVEEDORES:
            return PROVEEDORES[int(id)]
        return "", 404

    def delete(self, id):
        if int(id) in PROVEEDORES:
            del PROVEEDORES[int(id)]
            return '', 204
        return '', 404

    def put(self, id):
        if int(id) in PROVEEDORES:
            proveedor = PROVEEDORES[int(id)]
            date = request.get_json()
            proveedor.update(date)
            return proveedor, 201
        return '', 404

