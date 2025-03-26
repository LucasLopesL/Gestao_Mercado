from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash
from app.core.models import db, Seller
import random
from twilio.rest import Client
from flask_jwt_extended import create_access_token

app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)

# Função para enviar o código via Twilio
def enviar_codigo_ativacao(celular, codigo):
    account_sid = 'seu_account_sid'
    auth_token = 'seu_auth_token'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f"Seu código de ativação é {codigo}",
        from_='+1415XXXXXXX',  # Número do Twilio
        to=celular
    )
    return message.sid

@app.route('/api/sellers', methods=['POST'])
def criar_seller():
    data = request.get_json()
    codigo_ativacao = str(random.randint(1000, 9999))

    # Criar seller no banco
    seller = Seller(
        nome=data['nome'],
        cnpj=data['cnpj'],
        email=data['email'],
        celular=data['celular'],
        senha=generate_password_hash(data['senha']),
    )
    db.session.add(seller)
    db.session.commit()

    # Enviar código de ativação
    enviar_codigo_ativacao(data['celular'], codigo_ativacao)

    return jsonify({'message': 'Seller cadastrado com sucesso, código de ativação enviado!'})

if __name__ == '__main__':
    app.run(debug=True)

