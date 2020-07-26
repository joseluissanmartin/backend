
from flask import request, jsonify, Blueprint, current_app
import  json
import datetime
import jwt
import marshmallow
from functools import wraps
from project.models import Usuario
from project import db, bcrypt
from project.schemas import usuario_schema
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


blueprint = Blueprint("usuarios", __name__)#para generar las rutas

def usuario_a_dict(usuario):#el diccionario
    return {
    "id": usuario.id,
    "nombre": usuario.nombre,
    "email": usuario.email,
    "password": usuario.password,
    "fecha": usuario.fecha,
    "sistema_o": usuario.sistema_o,
    "procesador": usuario.procesador,
    "almacenamiento": usuario.almacenamiento,
    "ram": usuario.ram,
    "grafica": usuario.grafica,
    "direct_x": usuario.direct_x,
    "gusto": usuario.gusto}


def check_token():
    authorization = request.headers.get('Authorization')

    if authorization is None:
        return False

    partes = authorization.split(' ')
    if len(partes) != 2:
        return False

    if partes[0] != 'Bearer':
        return False

    token = partes[1]

    try:
        return jwt.decode(token, current_app.config['SECRET'])
    except:
        return False

#@blueprint.route("/inicio")#rutas
def index():
    return "<h1>Hola</h1>"


@blueprint.route("/registro", methods=["POST"])
def register():
    usuario = usuario_schema.load(request.json)

    db.session.add(usuario)#generador de sesion
    db.session.commit()

    return usuario_schema.dump(usuario), 201


@blueprint.route("/login/<id>", methods=["GET"])
def view(id):
    check_response = check_token()

    if check_response is False:#autenticador
        return "Unauthorized", 401

    if str(check_response["sub"]) != str(id):
        return "Forbidden", 403

    usuario =Usuario.query.get_or_404(id)

    respuesta = []

    respuesta.append({
                "id": usuario.id,
                "nombre": usuario.nombre,
                "email": usuario.email,
            })
    return jsonify(respuesta), 200



@blueprint.route("/ingresoEspecificaciones/<id>", methods=["PATCH"])
def patch(id):
    check_response = check_token()

    if check_response is False:
        return "Unauthorized", 401

    usuario =Usuario.query.get_or_404(id)
    datos= request.get_json()


    usuario.sistema_o = datos.get("sistema_o", usuario.sistema_o)
    usuario.procesador = datos.get("procesador", usuario.procesador)
    usuario.almacenamiento = datos.get("almacenamiento", usuario.almacenamiento)
    usuario.ram = datos.get("ram", usuario.ram)
    usuario.grafica = datos.get("grafica", usuario.grafica)
    usuario.direct_x = datos.get("direct_x", usuario.direct_x)

    db.session.add(usuario)
    db.session.commit()

    return usuario_a_dict(usuario), 200



@blueprint.route("/ingresoPreferencias/<id>", methods=["PATCH"])
def patch_gusto(id):
    check_response = check_token()

    if check_response is False:
        return "Unauthorized", 401

    usuario =Usuario.query.get_or_404(id)
    datos= request.get_json()

    usuario.gusto = datos.get("gusto", usuario.gusto)

    db.session.add(usuario)
    db.session.commit()

    return usuario_a_dict(usuario), 200


@blueprint.route('/login', methods=['GET', 'POST'])
def login():
    datos = request.get_json()

    email = datos['email']
    password = datos['password']
    nombre = datos['nombre']

    usuario = Usuario.query.filter_by(email = email, password=password).first()

    if usuario is None:
        return 'Not found', 404

    if bcrypt.check_password_hash(usuario.password, password) is False:
        return "not found", 404

    payload = {
        'sub': usuario.id,
        'name': usuario.nombre,
        'iat': datetime.datetime.now()
    }

    return jwt.encode(
        payload,
        current_app.config['SECRET'],
        algorithm='HS256')


@blueprint.route('/token', methods=['GET'])
def usuario(payload):
    usuario = Usuario.query.get_or_404(payload['sub'])

    return usuario_schema.dump(usuario), 200
