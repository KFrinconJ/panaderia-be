
# Importacion de los datos de la app
from __main__ import *
from helpers.helpers import *

clientesSQL = SqlUtilities("clientes", "sql10580635")


@app.route('/clientes', methods=['GET'])
# Funciones para realizar el CRUD
# Obtener todos los registros de cliente
def listar_clientes():
    try:

        columnNames = clientesSQL.getColumnNames()
        queryData = clientesSQL.selectAllQuery()

        resultData = jsonSqlAllQueryCreation(columnNames, queryData)

        return jsonify({
            'header': resultData[0],
            'clientes': resultData[1],
            'mensaje': 'Clientes listados correctamente'
        })
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})


# Obtener Cliente por cedula
@app.route('/clientes/<cedulaCliente>', methods=['GET'])
def obtener_cliente_cedula(cedulaCliente):
    try:
        columnNames = clientesSQL.getColumnNames()
        queryData = clientesSQL.selectByIdQuery(
            columnNames[0][0], cedulaCliente)

        resultData = jsonSqlAllQueryCreation(columnNames, queryData)

        return jsonify({
            'header': resultData[0],
            'cliente': resultData[1],
            'mensaje': 'Clientes listado correctamente'
        })
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})


# Enviar registro de un cliente
@app.route('/clientes', methods=['POST'])
def registrar_cliente():
    try:

        columnNames = clientesSQL.getColumnNames()
        queryDrawData = requestSql(columnNames)

        resultPassableParams = insert_params(queryDrawData[1])

        print(resultPassableParams)

        clientesSQL.insertQuery(resultPassableParams)

        return jsonify({
            'mensaje': 'Clientes registrado correctamente'
        })

    except Exception as ex:
        return jsonify({'mensaje': 'Error'})


# Actualizar cliente
@app.route('/clientes/<cedulaCliente>', methods=['PUT'])
def actualizar_cliente(cedulaCliente):
    try:

        columnNames = clientesSQL.getColumnNames()
        queryDrawData = requestSql(columnNames)
        resultPassableParams = update_params(
            queryDrawData[0], queryDrawData[1])

        clientesSQL.updateQuery(
            columnNames[0][0], cedulaCliente, resultPassableParams)

        return jsonify({
            'mensaje': 'Clientes registrado correctamente'
        })

    except Exception as ex:
        return jsonify({'mensaje': 'Error'})


# Borrar cliente
@app.route('/clientes/<cedulaCliente>', methods=['DELETE'])
def eliminar_cliente(cedulaCliente):
    try:
        columnNames = clientesSQL.getColumnNames()
        clientesSQL.deleteQuery(columnNames[0][0], cedulaCliente)

        return jsonify({
            'mensaje': 'Cliente eliminado'
        })

    except Exception as ex:
        return jsonify({'mensaje': 'Error'})
