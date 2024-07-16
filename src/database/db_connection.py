import mysql.connector

DB_CONFIG={
    'host' : 'NSJA.mysql.pythonanywhere-services.com',
    'user' : 'NSJA',
    'password' : 'Prueba1234!',
    'database' : 'NSJA$pruebadb'
    
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
