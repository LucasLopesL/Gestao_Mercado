from twilio.rest import Client

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
