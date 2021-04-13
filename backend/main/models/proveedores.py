from .. import db


class Proveedores(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Proveedores: %r %r %r >' % (self.nombre, self.nombre, self.telefono)

    def to_json(self):
        proveedor_json = {
            'id': self.id,
            'nombre': str(self.nombre),
            'telefono': str(self.telefono)

        }
        return proveedor_json

    def from_json(proveedor_json):
        id = proveedor_json.get('id')
        nombre = proveedor_json.get('nombre')
        telefono = proveedor_json.get('telefono')
        return Proveedores(id=id,
                           nombre=nombre,
                           telefono=telefono,
                           )