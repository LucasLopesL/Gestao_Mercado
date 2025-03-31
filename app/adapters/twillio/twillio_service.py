from twilio.rest import Client

def enviar_codigo_ativacao(celular, codigo):
    account_sid = 'ACfbef0f945503dc98894a6c205f1e8560'
    auth_token = '8299a56fc293fabeec3cacc603c2dd31'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f"Seu código de ativação é {codigo}",
        from_='+14155238886',  # Número do Twilio
        to=celular
    )
    return message.sid
