from flask import Blueprint,request,jsonify
from src.controller.product_controller import *

product_bp=Blueprint('product_bp', __name__, url_prefix='/products') #con esto se podia ver en json
# product_bp=Blueprint('products',__name__, template_folder='../templates')

@product_bp.route('/', methods=['GET'])
def get_all_products_route():
    products=get_all_products_controller()
    return products
@product_bp.route('/<int:product_id>', methods=['GET'])
def get_product_by_id_route(product_id):
    return get_product_by_id_controller(product_id)

@product_bp.route('/', methods=['POST'])
def create_product_route():
    return create_product_controller()

@product_bp.route('/<int:product_id>', methods=['PUT'])
def update_product_route(product_id):
    return update_product_controller(product_id)

@product_bp.route('/delete_product/<int:product_id>', methods=['DELETE'])
def delete_product_route(product_id):
    return delete_product_controller(product_id)