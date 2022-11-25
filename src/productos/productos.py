
# Importacion de los datos de la app
from __main__ import *
from helpers.helpers import *

productosSQL = SqlUtilities("productos", "marcellareal")


@app.route('/productos', methods=['GET'])
# Funciones para realizar el CRUD
# Obtener todos los registros de cliente
def listar_productos():
    try:

        columnNames = productosSQL.getColumnNames()
        queryData = productosSQL.selectAllQuery()

        resultData = jsonSqlAllQueryCreation(columnNames, queryData)

        return jsonify({
            'header': resultData[0],
            'productos': resultData[1],
            'mensaje': 'Productos listados correctamente'
        })
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})


# Obtener Cliente por cedula
@app.route('/productos/<codigoProducto>', methods=['GET'])
def obtener_producto_codigo(codigoProducto):
    try:
        columnNames = productosSQL.getColumnNames()
        queryData = productosSQL.selectByIdQuery(
            columnNames[0][0], codigoProducto)

        resultData = jsonSqlAllQueryCreation(columnNames, queryData)

        return jsonify({
            'header': resultData[0],
            'producto': resultData[1],
            'mensaje': 'Producto listado correctamente'
        })
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})


# Enviar registro de un cliente
@app.route('/productos', methods=['POST'])
def registrar_producto():
    try:

        columnNames = productosSQL.getColumnNames()
        queryDrawData = requestSql(columnNames)

        resultPassableParams = insert_params(queryDrawData[1])

        print(resultPassableParams)

        productosSQL.insertQuery(resultPassableParams)

        return jsonify({
            'mensaje': 'Producto registrado correctamente'
        })

    except Exception as ex:
        return jsonify({'mensaje': 'Error'})


# Actualizar cliente
@app.route('/productos/<codigoProducto>', methods=['PUT'])
def actualizar_producto(codigoProducto):
    try:

        columnNames = productosSQL.getColumnNames()
        queryDrawData = requestSql(columnNames)
        resultPassableParams = update_params(
            queryDrawData[0], queryDrawData[1])

        productosSQL.updateQuery(
            columnNames[0][0], codigoProducto, resultPassableParams)

        return jsonify({
            'mensaje': 'Producto actualizado correctamente'
        })

    except Exception as ex:
        return jsonify({'mensaje': 'Error'})


# Borrar cliente
@app.route('/productos/<codigoProducto>', methods=['DELETE'])
def eliminar_producto(codigoProducto):
    try:
        columnNames = productosSQL.getColumnNames()
        productosSQL.deleteQuery(columnNames[0][0], codigoProducto)

        return jsonify({
            'mensaje': 'Producto eliminado'
        })

    except Exception as ex:
        return jsonify({'mensaje': 'Error'})
