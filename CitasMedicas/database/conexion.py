import mysql.connector
from mysql.connector import Error

def conectado():
    try:
        connection = mysql.connector.connect(
            host = 'localhost',
            database = 'citasmedicas',
            user = '1234',
            password = '1234'
        )
        if connection.is_connected():
            db_info = connection.get_server_info()
            print("Conectado a MYSQL" , db_info)
            return connection
    except Error as e:
        print("Error en el momento de conexión con la base de datos")
        return e