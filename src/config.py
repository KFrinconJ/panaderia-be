#Datos aislados de la aplicacion
#Activar el virtual env .\env\Scripts\activate
#Desactivar el entorno virtual deactivate

class DevelopmentConfig():
    #Modo de depuracion
    DEBUG = True

    #Datos de la base de datos
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'marcellareal'

config = {
    'development':DevelopmentConfig
}