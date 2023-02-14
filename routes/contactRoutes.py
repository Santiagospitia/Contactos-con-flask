from flask import jsonify, Flask, request
from flask import Blueprint
import controllers.contactController as contactController

contact_api = Blueprint('contact_api', __name__)

@contact_api.route('/contactos', methods=['GET'])
def contactos():
    parametros = request.args
    id_usuario = parametros['id_usuario']
    campo = parametros['campo']
    orden = parametros['orden']
    contactos = contactController.seleccionarContactos(id_usuario, campo, orden)
    return jsonify(contactos)

@contact_api.route('/contacto', methods=['GET'])
def getContacto():
    parametros = request.args
    id_contacto = parametros['id_contacto']
    contacto = contactController.seleccionarContacto(id_contacto)
    return jsonify(contacto)

@contact_api.route('/contactostr', methods=['GET'])
def getContactoStr():
    parametros = request.args
    id_usuario = parametros['id_usuario']
    value = parametros['value']
    contactos = contactController.busquedaContactos(id_usuario, value)
    return jsonify(contactos)

@contact_api.route('/contacto', methods=['POST'])
def insertContacto():
    parametros = request.args
    id_usuario = parametros['id_usuario']
    nombre = parametros['nombre']
    apellidos = parametros['apellidos']
    direccion = parametros['direccion']
    email = parametros['email']
    telefono = parametros['telefono']

    result = contactController.insertarContacto(id_usuario, nombre, apellidos, direccion, email, telefono)

    return jsonify({'result':result})

@contact_api.route('/contacto', methods=['PUT'])
def updateContacto():
    parametros = request.args
    id_contacto = parametros['id']
    nombre = parametros['nombre']
    apellidos = parametros['apellidos']
    direccion = parametros['direccion']
    email = parametros['email']
    telefono = parametros['telefono']

    result = contactController.actualizar_contacto(id_contacto,nombre,apellidos,direccion,email,telefono)

    return jsonify({'result':result})

@contact_api.route('/contacto', methods=['DELETE'])
def deleteContacto():
    parametros = request.args
    id_usuario = parametros['id_usuario']
    id_contacto = parametros['id_contacto']
    result = contactController.eliminar_contacto(id_usuario,id_contacto)
    return jsonify({'result':result})

