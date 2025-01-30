import mysql.connector
from mysql.connector import Error

def conectado():
    try:
        connection = mysql.connector.connect(
            host = 'mysql_citas_medicas',
            database = 'citas_medicas',
            user = 'root',
            password = 'blas1234'
        )
        if connection.is_connected():
            db_info = connection.get_server_info()
            print("Conectado a MYSQL" , db_info)
            return connection
    except Error as e:
        print("Error en el momento de conexión con la base de datos")
        return e