from __main__ import *


class SqlUtilities:
    def __init__(self, table_name, schema_name):
        self.table_name = table_name
        self.schema_name = schema_name

    # Obtener el nombre de las columnas de la tabla
    def getColumnNames(self):
        cur = mysql.connection.cursor()
        query = f'''SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE 
                TABLE_SCHEMA = "{self.schema_name}" and TABLE_NAME = "{self.table_name}" 
                order by ORDINAL_POSITION'''
        cur.execute(query)
        data = cur.fetchall()

        return (data)

    # Obtener todos los registros de la tabla
    def selectAllQuery(self):
        # cur inicializa el cursor de la base de datos
        cur = mysql.connection.cursor()
        # Consulta que trae todos las filas de clientes
        query = f'SELECT * FROM {self.table_name}'
        # Ejecuta la consulta
        cur.execute(query)
        # Trae todas las filas del conjunto
        data = cur.fetchall()

        return (data)

    # Eliminar el registro de acuerdo al id

    def deleteQuery(self, id_column_name, id_column_value):
        cur = mysql.connection.cursor()
        query = f'DELETE FROM {self.table_name} WHERE {id_column_name} = "{id_column_value}";'
        cur.execute(query)
        mysql.connection.commit()  # Confima la accion de insercion

    # Seleccionar un registro por id
    def selectByIdQuery(self, id_column_name, id_column_value):
        cur = mysql.connection.cursor()
        query = f'SELECT * FROM {self.table_name} WHERE {id_column_name} = "{id_column_value}"'
        cur.execute(query)
        data = cur.fetchall()
        return (data)

    # Actualizar un registro de acuerdo a su id
    def updateQuery(self, id_column_name, id_column_value, passableParams):
        cur = mysql.connection.cursor()
        query = f'UPDATE {self.table_name} SET {passableParams} WHERE {id_column_name} = "{id_column_value}"'
        cur.execute(query)
        mysql.connection.commit()  # Confima la accion de insercion

    # Ingrear un registro
    def insertQuery(self, passableParams):
        cur = mysql.connection.cursor()
        query = f'INSERT INTO {self.table_name} VALUES ({passableParams})'
        cur.execute(query)
        mysql.connection.commit()  # Confima la accion de insercion


def jsonSqlAllQueryCreation(col_name_collection, data_collection):
    col_name_array = []
    data_array = []

    for col in col_name_collection:
        col_name_array.append(col[0])

    if len(data_collection) > 1:
        for row in range(len(data_collection)):
            item = {}
            row_data = data_collection[row]
            for c in range(len(col_name_array)):
                item[col_name_array[c]] = row_data[c]
            data_array.append(item)

    else:
        item = {}
        row_data = data_collection[0]
        for c in range(len(col_name_array)):
            item[col_name_array[c]] = row_data[c]
        data_array.append(item)

    return (col_name_array, data_array)


def requestSql(col_name_collection):
    col_name_array = []
    request_values_array = []

    for col in col_name_collection:
        col_name_array.append(col[0])

    for value in col_name_array:
        request_values_array.append(request.json[value])

    return (col_name_array, request_values_array)


def update_params(arrayA, arrayB):
    paramsList = []
    for i in range(len(arrayA)):
        paramsList.append(f'{arrayA[i]} = "{arrayB[i]}"')

    return ", ".join(paramsList)


def insert_params(arrayA):
    paramsList = []
    for data in (arrayA):
        paramsList.append(f'"{data}"')

    return ", ".join(paramsList)
