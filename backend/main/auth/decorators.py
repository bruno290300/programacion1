from .. import jwt
from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from functools import wraps

def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        #Verificar que el JWT es correcto
        verify_jwt_in_request()
        #Obtener claims de adentro del JWT
        claims = get_jwt()
        #Verificar que el rol sea admin
        if claims['rol'] == "admin" :
            #Ejecutar función
            return fn(*args, **kwargs)
        else:
            return 'Only admins can access', 403
    return wrapper


def proveedor_or_admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if claims['rol'] == 'proveedor' or claims['rol'] == 'admin':
            return fn(*args, **kwargs)
        else:
            return 'Only admins or proveedores can access', 403
    return wrapper

def proveedor_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if claims['rol'] == 'proveedor':
            return fn(*args, **kwargs)
        else:
            return 'Only proveedores can access', 403
    return wrapper

def cliente_or_admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if claims['rol'] == 'cliente' or claims['rol'] == 'admin':
            return fn(*args, **kwargs)
        else:
            return 'Only admins or clientes can access', 403
    return wrapper

def cliente_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt()
        if claims['rol'] == 'cliente':
            return fn(*args, **kwargs)
        else:
            return 'Only cliente can accesss', 403
    return wrapper

@jwt.user_identity_loader


def user_identity_lookup(usuario):
    #Definir ID como atributo identificatorio
    return usuario.id

@jwt.additional_claims_loader
def add_claims_to_access_token(usuario):
    claims = {
        'rol': usuario.rol,
        'id': usuario.id,
        'mail': usuario.mail
    }
    
    return claims