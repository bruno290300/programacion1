from .. import db

class Compra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha_hora_compra = db.Column(db.DateTime, nullable=False)
    retirado = db.Column(db.Boolean, default=False, nullable=False)
    bolsonid = db.Column(db.Integer, db.ForeignKey('bolson.id'), nullable=False)
    bolson = db.relationship('Bolson', back_populates= 'compras', uselist=False, single_parent=True)

    def __repr__(self):
        return f'Compra: {self.fecha_hora_compra}, {self.retirado,}, {self.bolsonid}'

    def to_json(self):
        compra_json = {
            'id': self.id,
            'fecha_hora_compra': self.fecha_hora_compra,
            'retirado': self.retirado,
            'bolsonid': self.bolsonid,
        }

    @staticmethod
    def from_json(compra_json):
        id = compra_json.get('id')
        fecha_hora_compra = compra_json.get('fecha_hora_compra')
        retirado = compra_json.get('retirado')
        bolsonid = compra_json.get('bolsonid')
        return Compra(
            id = id,
            fecha_hora_compra = fecha_hora_compra,
            retirado = retirado,
            bolsonid = bolsonid
        )              