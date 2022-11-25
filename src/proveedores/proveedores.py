
# Importacion de los datos de la app
from __main__ import *
from helpers.helpers import *

proveedoresSQL = SqlUtilities("proveedores", "marcellareal")


@app.route('/proveedores', methods=['GET'])
# Funciones para realizar el CRUD
# Obtener todos los registros de cliente
def listar_proveedores():
    try:

        columnNames = proveedoresSQL.getColumnNames()
        queryData = proveedoresSQL.selectAllQuery()

        resultData = jsonSqlAllQueryCreation(columnNames, queryData)

        return jsonify({
            'header': resultData[0],
            'proveedores': resultData[1],
            'mensaje': 'Proveedores listados correctamente'
        })
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})


# Obtener Cliente por cedula
@app.route('/proveedores/<nitProveedor>', methods=['GET'])
def obtener_proveedor_codigo(nitProveedor):
    try:
        columnNames = proveedoresSQL.getColumnNames()
        queryData = proveedoresSQL.selectByIdQuery(
            columnNames[0][0], nitProveedor)

        resultData = jsonSqlAllQueryCreation(columnNames, queryData)

        return jsonify({
            'header': resultData[0],
            'proveedor': resultData[1],
            'mensaje': 'proveedor listado correctamente'
        })
    except Exception as ex:
        return jsonify({'mensaje': 'Error'})


# Enviar registro de un cliente
@app.route('/proveedores', methods=['POST'])
def registrar_proveedor():
    try:

        columnNames = proveedoresSQL.getColumnNames()
        queryDrawData = requestSql(columnNames)

        resultPassableParams = insert_params(queryDrawData[1])

        print(resultPassableParams)

        proveedoresSQL.insertQuery(resultPassableParams)

        return jsonify({
            'mensaje': 'Proveedor registrado correctamente'
        })

    except Exception as ex:
        return jsonify({'mensaje': 'Error'})


# Actualizar cliente
@app.route('/proveedores/<nitProveedor>', methods=['PUT'])
def actualizar_proveedor(nitProveedor):
    try:

        columnNames = proveedoresSQL.getColumnNames()
        queryDrawData = requestSql(columnNames)
        resultPassableParams = update_params(
            queryDrawData[0], queryDrawData[1])

        proveedoresSQL.updateQuery(
            columnNames[0][0], nitProveedor, resultPassableParams)

        return jsonify({
            'mensaje': 'Proveedor actualizado correctamente'
        })

    except Exception as ex:
        return jsonify({'mensaje': 'Error'})


# Borrar cliente
@app.route('/proveedores/<nitProveedor>', methods=['DELETE'])
def eliminar_proveedor(nitProveedor):
    try:
        columnNames = proveedoresSQL.getColumnNames()
        proveedoresSQL.deleteQuery(columnNames[0][0], nitProveedor)

        return jsonify({
            'mensaje': 'Proveedor eliminado'
        })

    except Exception as ex:
        return jsonify({'mensaje': 'Error'})
