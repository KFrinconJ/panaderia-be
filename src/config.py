#Datos aislados de la aplicacion
#Activar el virtual env .\env\Scripts\activate
#Desactivar el entorno virtual deactivate

class DevelopmentConfig():
    #Modo de depuracion
    DEBUG = True

    #Datos de la base de datos
    MYSQL_HOST = 'sql10.freemysqlhosting.net'
    MYSQL_USER = 'sql10580635'
    MYSQL_PASSWORD = 'ThfKgwHI3E'
    MYSQL_DB = 'sql10580635'

config = {
    'development':DevelopmentConfig
}