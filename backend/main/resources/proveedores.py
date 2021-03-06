from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import UsuarioModel
from flask_jwt_extended import jwt_required, get_jwt_identity
from main.auth.decorators import admin_required




class Proveedores(Resource):
    """
    def get(self):
        return PROVEEDORES

    def post(self):
        proveedor = request.get_json()
        id = int(max(PROVEEDORES.keys())) + 1
        PROVEEDORES[id] = proveedor
        return PROVEEDORES[id], 201
    """
    @jwt_required()
    def get(self):
        proveedores = db.session.query(UsuarioModel).filter(UsuarioModel.rol == 'proveedor')
        return jsonify([proveedor.to_json() for proveedor in proveedores])
    @jwt_required()
    def post(self):
        proveedor = UsuarioModel.from_json(request.get_json())
        db.session.add(proveedor)
        db.session.commit()
        return proveedor.to_json(), 201

class Proveedor(Resource):
    """
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
    """
    @jwt_required()
    def get(self, id):
        proveedor = db.session.query(UsuarioModel).get_or_404(id)
        return proveedor.to_json()
    @admin_required
    def delete(self, id):
        proveedor = db.session.query(UsuarioModel).get_or_404(id)
        db.session.delete(proveedor)
        db.session.commit()
        return '', 204
    @jwt_required()
    def put(self, id):
        proveedor = db.session.query(UsuarioModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(proveedor, key, value)
        db.session.add(proveedor)
        db.session.commit()
        return proveedor.to_json(), 201
