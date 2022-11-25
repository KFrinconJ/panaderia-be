
# Importacion de los datos de la app
from __main__ import *
from helpers.helpers import *

ventasSQL = SqlUtilities("ventas", "marcellareal")


@app.route('/ventas', methods=['GET'])
# Funciones para realizar el CRUD
# Obtener todos los registros de cliente
def listar_ventas():
    try:

        columnNames = ventasSQL.getColumnNames()
        queryData = ventasSQL.selectAllQuery()

        resultData = jsonSqlAllQueryCreation(columnNames, queryData)

        return jsonify({
            'header': resultData[0],
            'ventas': resultData[1],
            'mensaje': 'ventas listadas correctamente'
        })
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})


# Obtener Cliente por cedula
@app.route('/ventas/<codigoVenta>', methods=['GET'])
def obtener_venta_codigo(codigoVenta):
    try:
        columnNames = ventasSQL.getColumnNames()
        queryData = ventasSQL.selectByIdQuery(
            columnNames[0][0], codigoVenta)

        resultData = jsonSqlAllQueryCreation(columnNames, queryData)

        return jsonify({
            'header': resultData[0],
            'venta': resultData[1],
            'mensaje': 'venta listado correctamente'
        })
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})


# Enviar registro de un cliente
@app.route('/ventas', methods=['POST'])
def registrar_venta():
    try:

        columnNames = ventasSQL.getColumnNames()
        queryDrawData = requestSql(columnNames)

        resultPassableParams = insert_params(queryDrawData[1])

        print(resultPassableParams)

        ventasSQL.insertQuery(resultPassableParams)

        return jsonify({
            'mensaje': 'venta registrado correctamente'
        })

    except Exception as ex:
        return jsonify({'mensaje': 'Error'})


# Actualizar cliente
@app.route('/ventas/<codigoVenta>', methods=['PUT'])
def actualizar_venta(codigoVenta):
    try:

        columnNames = ventasSQL.getColumnNames()
        queryDrawData = requestSql(columnNames)
        resultPassableParams = update_params(
            queryDrawData[0], queryDrawData[1])

        ventasSQL.updateQuery(
            columnNames[0][0], codigoVenta, resultPassableParams)

        return jsonify({
            'mensaje': 'venta actualizado correctamente'
        })

    except Exception as ex:
        return jsonify({'mensaje': 'Error'})


# Borrar cliente
@app.route('/ventas/<codigoVenta>', methods=['DELETE'])
def eliminar_venta(codigoVenta):
    try:
        columnNames = ventasSQL.getColumnNames()
        ventasSQL.deleteQuery(columnNames[0][0], codigoVenta)

        return jsonify({
            'mensaje': 'venta eliminado'
        })

    except Exception as ex:
        return jsonify({'mensaje': 'Error'})
