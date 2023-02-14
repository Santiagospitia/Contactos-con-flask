from flask import Flask, jsonify, request
from flask import Blueprint  #permite enlazar las dos rutas con el fichero main.py

pruebas_api = Blueprint('pruebas_api', __name__)

@pruebas_api.route("/", methods=['GET']) #decorador de una funcion, por defecto está GET
def prueba():
    prueba = {
        "nombre":"api-rest"      #Objeto json
    }  
    return jsonify(prueba) #retornando el objeto como json

@pruebas_api.route("/usuarios", methods=['GET']) #decorador de una funcion
def prueba2():
    return "Hola Usuarios"