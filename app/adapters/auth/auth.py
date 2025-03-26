from flask_jwt_extended import JWTManager, create_access_token
from flask import Flask, request, jsonify
from app.core.models import db, Seller
from werkzeug.security import check_password_hash

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)

jwt = JWTManager(app)

@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json()
    seller = Seller.query.filter_by(email=data['email']).first()

    if seller and check_password_hash(seller.senha, data['senha']):
        if seller.status == 'Inativo':
            return jsonify({'message': 'Conta inativa. Ative sua conta primeiro.'}), 401

        access_token = create_access_token(identity=seller.id)
        return jsonify({'access_token': access_token})

    return jsonify({'message': 'Credenciais inválidas!'}), 401
