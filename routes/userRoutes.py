from flask import jsonify, Flask, request
from flask import Blueprint
import controllers.userController as userController

user_api = Blueprint('user_api', __name__)

@user_api.route('/usuario', methods=['GET'])
def getUsuario():
    parametros = request.args
    print("Soy los parametros: ", parametros)
    email = parametros['email']
    password = parametros['password']
    result = userController.seleccionarUsuario(email, password)
    return jsonify({'result':result})