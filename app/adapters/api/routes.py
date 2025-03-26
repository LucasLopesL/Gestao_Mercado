from flask import Blueprint, request, jsonify, render_template
from flask_jwt_extended import get_jwt_identity, jwt_required, create_access_token
from app.core.services.services import validar_login
from app.core.repositories.repositories import criar_seller, criar_produto
from werkzeug.security import generate_password_hash

api = Blueprint('api', __name__, template_folder="../../web/templates")

@api.route("/")
def home():
    return render_template("index.html")

@api.route('/api/sellers', methods=['POST'])
def criar_seller_route():
    data = request.get_json()
    data['senha'] = generate_password_hash(data['senha'])
    seller = criar_seller(data)
    return jsonify({'message': 'Seller cadastrado com sucesso!'}), 201

@api.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    seller = validar_login(data['email'], data['senha'])
    if seller:
        access_token = create_access_token(identity=seller.id)
        return jsonify({'access_token': access_token}), 200
    return jsonify({'message': 'Credenciais inválidas!'}), 401

@api.route('/api/products', methods=['POST'])
@jwt_required()
def cadastrar_produto_route():
    data = request.get_json()
    seller_id = get_jwt_identity()  # Obter seller_id do JWT
    produto = criar_produto(data, seller_id)
    return jsonify({'message': 'Produto cadastrado com sucesso!'}), 201


