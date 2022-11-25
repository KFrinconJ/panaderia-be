
# Importacion de los datos de la app
from __main__ import *
from helpers.helpers import *

usuariosSQL = SqlUtilities("usuarios", "marcellareal")


@app.route('/usuarios', methods=['GET'])
# Funciones para realizar el CRUD
# Obtener todos los registros de cliente
def listar_usuarios():
    try:

        columnNames = usuariosSQL.getColumnNames()
        queryData = usuariosSQL.selectAllQuery()

        resultData = jsonSqlAllQueryCreation(columnNames, queryData)

        return jsonify({
            'header': resultData[0],
            'usuarios': resultData[1],
            'mensaje': 'Usuarios listados correctamente'
        })
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})


# Obtener Cliente por cedula
@app.route('/usuarios/<cedulaUsuario>', methods=['GET'])
def obtener_usuario_codigo(cedulaUsuario):
    try:
        columnNames = usuariosSQL.getColumnNames()
        queryData = usuariosSQL.selectByIdQuery(
            columnNames[0][0], cedulaUsuario)

        resultData = jsonSqlAllQueryCreation(columnNames, queryData)

        return jsonify({
            'header': resultData[0],
            'usuario': resultData[1],
            'mensaje': 'usuario listado correctamente'
        })
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})


# Enviar registro de un cliente
@app.route('/usuarios', methods=['POST'])
def registrar_usuario():
    try:

        columnNames = usuariosSQL.getColumnNames()
        queryDrawData = requestSql(columnNames)

        resultPassableParams = insert_params(queryDrawData[1])

        print(resultPassableParams)

        usuariosSQL.insertQuery(resultPassableParams)

        return jsonify({
            'mensaje': 'Usuario registrado correctamente'
        })

    except Exception as ex:
        return jsonify({'mensaje': 'Error'})


# Actualizar cliente
@app.route('/usuarios/<cedulaUsuario>', methods=['PUT'])
def actualizar_usuario(cedulaUsuario):
    try:

        columnNames = usuariosSQL.getColumnNames()
        queryDrawData = requestSql(columnNames)
        resultPassableParams = update_params(
            queryDrawData[0], queryDrawData[1])

        usuariosSQL.updateQuery(
            columnNames[0][0], cedulaUsuario, resultPassableParams)

        return jsonify({
            'mensaje': 'Usuario actualizado correctamente'
        })

    except Exception as ex:
        return jsonify({'mensaje': 'Error'})


# Borrar cliente
@app.route('/usuarios/<cedulaUsuario>', methods=['DELETE'])
def eliminar_usuario(cedulaUsuario):
    try:
        columnNames = usuariosSQL.getColumnNames()
        usuariosSQL.deleteQuery(columnNames[0][0], cedulaUsuario)

        return jsonify({
            'mensaje': 'Usuario eliminado'
        })

    except Exception as ex:
        return jsonify({'mensaje': 'Error'})
