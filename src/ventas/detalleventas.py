
# Importacion de los datos de la app
from __main__ import *
from helpers.helpers import *

detalleventasSQL = SqlUtilities("detalleventas", "marcellareal")


@app.route('/detalleventas', methods=['GET'])
# Funciones para realizar el CRUD
# Obtener todos los registros de cliente
def listar_detalleventa():
    try:

        columnNames = detalleventasSQL.getColumnNames()
        queryData = detalleventasSQL.selectAllQuery()

        resultData = jsonSqlAllQueryCreation(columnNames, queryData)

        return jsonify({
            'header': resultData[0],
            'detalleventas': resultData[1],
            'mensaje': 'detalleventaa listados correctamente'
        })
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})


# Obtener Cliente por cedula
@app.route('/detalleventas/<codigodetalleventa>', methods=['GET'])
def obtener_detalleventa_codigo(codigodetalleventa):
    try:
        columnNames = detalleventasSQL.getColumnNames()
        queryData = detalleventasSQL.selectByIdQuery(
            columnNames[0][0], codigodetalleventa)

        resultData = jsonSqlAllQueryCreation(columnNames, queryData)

        return jsonify({
            'header': resultData[0],
            'detalleventa': resultData[1],
            'mensaje': 'detalleventa listado correctamente'
        })
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})


# Enviar registro de un cliente
@app.route('/detalleventas', methods=['POST'])
def registrar_detalleventa():
    try:

        columnNames = detalleventasSQL.getColumnNames()
        queryDrawData = requestSql(columnNames)

        resultPassableParams = insert_params(queryDrawData[1])

        print(resultPassableParams)

        detalleventasSQL.insertQuery(resultPassableParams)

        return jsonify({
            'mensaje': 'Usuario registrado correctamente'
        })

    except Exception as ex:
        return jsonify({'mensaje': 'Error'})


# Actualizar cliente
@app.route('/detalleventas/<codigodetalleventa>', methods=['PUT'])
def actualizar_detalleventa(codigodetalleventa):
    try:

        columnNames = detalleventasSQL.getColumnNames()
        queryDrawData = requestSql(columnNames)
        resultPassableParams = update_params(
            queryDrawData[0], queryDrawData[1])

        detalleventasSQL.updateQuery(
            columnNames[0][0], codigodetalleventa, resultPassableParams)

        return jsonify({
            'mensaje': 'detalleventa actualizado correctamente'
        })

    except Exception as ex:
        return jsonify({'mensaje': 'Error'})


# Borrar cliente
@app.route('/detalleventas/<codigodetalleventa>', methods=['DELETE'])
def eliminar_detalleventa(codigodetalleventa):
    try:
        columnNames = detalleventasSQL.getColumnNames()
        detalleventasSQL.deleteQuery(columnNames[0][0], codigodetalleventa)

        return jsonify({
            'mensaje': 'detalleventa eliminado'
        })

    except Exception as ex:
        return jsonify({'mensaje': 'Error'})
