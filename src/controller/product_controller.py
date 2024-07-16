from flask import jsonify, request
from src.services.product_service import get_all_products, get_product_by_id, update_product,create_product, delete_product
from src.model.product_model import Product

def get_all_products_controller():
    products=get_all_products()
    return jsonify(products)

def get_product_by_id_controller(product_id):
    product= get_product_by_id(product_id)

    if product:
        return jsonify(product)
    else:
        return jsonify({"error" : "Producto no encontrado"}),404
    
def create_product_controller():
    data=request.get_json()
    product=Product(None,data['amount'],data['price'], data['description'], data['category'])
    if create_product(product):
        return jsonify({"message":"Producto creado exitosamente"})
    else:
        return jsonify({"error":"Error al crear el producto"}),500
    
def update_product_controller(product_id):
    data= request.get_json()
    product=Product(product_id, data['amount'], data['price'], data['description'], data['category'] )
    if update_product(product):
        return jsonify({"message":"Producto actualizado correwctamente"})
    else:
        return jsonify({"error":"No se pudo actualizar el producto"}),500
    
def delete_product_controller(product_id):
    if delete_product(product_id):
        return jsonify({"message": "producto eliminado"})
    else:
        return jsonify({"error": "no se pudo eliminar el producto"}), 500
    