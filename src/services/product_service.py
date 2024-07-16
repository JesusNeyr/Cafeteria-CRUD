from src.database.db_connection import connect
from src.model.product_model import Product
import mysql.connector
def get_all_products():
    try:
        connection=connect()
        if connection:
            cursor=connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM productos")
            products= cursor.fetchall()
            return products
    except Exception as ex:
        print(f'Error al cargar productos: {ex}')

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

def get_product_by_id(product_id):
    try:
        connection= connect()
        if connection:
            cursor=connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM productos WHERE id = %s",(product_id,))
            product=cursor.fetchone()
            return product
    except Exception as ex:
        print(f'error al consultar el producto con id {product_id}:{ex}')
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
def create_product(product):
    try:
        connection=connect()
        if connection:
            cursor=connection.cursor(dictionary=True)
            sql=("INSERT INTO productos (amount, price,description,category) VALUES (%s,%s,%s,%s)")
            data=(product.amount, product.price, product.description, product.category)
            cursor.execute(sql,data)
            connection.commit()
            return True
    except Exception as ex:
        print(f'Error al crear el producto: {ex}')
        return False
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
def update_product(product):
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor(dictionary=True)
            sql = "UPDATE productos SET amount = %s, price = %s, description = %s, category = %s WHERE id = %s"
            data = (product.amount, product.price, product.description, product.category, product.id)
            cursor.execute(sql, data)
            connection.commit()
            return True
    except Exception as ex:
        print(f'Error al actualizar el producto: {ex}')
        return False
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

def delete_product(product_id):
    try:
        connection = connect()
        if connection:
            cursor = connection.cursor(dictionary=True)
            cursor.execute('DELETE FROM productos WHERE id = %s', (product_id,))
            connection.commit()
            return True
    except Exception as ex:
        print(f'Error al eliminar el producto: {ex}')
        return False
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
