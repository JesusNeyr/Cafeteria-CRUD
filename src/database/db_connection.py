import mysql.connector

DB_CONFIG={
    'host' : '127.0.0.1',
    'user' : 'root',
    'password' : '',
    'database' : 'pruebadb'
    
}

#conectamos la base de datos
def connect():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f'Conectado al servidor MySQL versión {db_info}')
            return connection
    except Exception as e:
        print(f'Error al conectar a la base de datos: {e}')
        return None
