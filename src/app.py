from flask import Flask ,jsonify, request
from flask_mysqldb import MySQL
from config import config



app = Flask(__name__)
# Conexion con la base datos
mysql = MySQL(app)

from clientes.clientes import *
from productos.productos import *
from proveedores.proveedores import *
from usuarios.usuarios import *
from ventas.ventas import *
from ventas.detalleventas import *


def page_not_found(error):
    return '<h1>Página no encontrada</h1>'


if __name__ == '__main__':
    # Uso de la configuración externa creada en el objeto config
    app.config.from_object(config['development'])
    app.register_error_handler(404, page_not_found)
    # Inicia la aplicación
    app.run()
