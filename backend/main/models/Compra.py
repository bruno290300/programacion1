from .. import db
from datetime import datetime
from . import  BolsonModel

class Compra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha_hora_compra = db.Column(db.DateTime, nullable = False)
    retirado = db.Column(db.Boolean, default=False, nullable=False)
    usuarioId = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    usuario = db.relationship('Usuario', back_populates="compras", uselist=False, single_parent=True)
    bolsonid = db.Column(db.Integer, db.ForeignKey('bolson.id'), nullable=False)
    bolson = db.relationship('Bolson', back_populates= 'compras', uselist=False, single_parent=True)
    usuario= db.relationship('Usuario', back_populates='compras', uselist=False, single_parent=True)
    def __repr__(self):
        return f'Compra: {self.id}, {self.fecha_hora_compra}, {self.retirado,}, {self.usuario.to_json()},{self.bolson.to_json()}'

    def to_json(self):
        compra_json = {
            'id': self.id,
            'fecha_hora_compra': self.fecha_hora_compra.strftime('%Y-%m-%d'),
            'retirado': self.retirado,
            'usuario': self.usuario.to_json(),
            'bolson': self.bolson.to_json()

        }
        return compra_json

    @staticmethod
    def from_json(compra_json):
        id = compra_json.get('id')
        fecha_hora_compra = datetime.strptime(compra_json.get('fecha_hora_compra'), '%Y-%m-%d')
        retirado = compra_json.get('retirado')
        bolsonid = compra_json.get('bolsonid')
        usuarioId = compra_json.get('usuarioId')
        return Compra(
            id = id,
            fecha_hora_compra = fecha_hora_compra,
            retirado = retirado,
            bolsonid = bolsonid,
            usuarioId = usuarioId
        )          