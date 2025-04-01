from flask_jwt_extended import JWTManager

jwt = JWTManager()

def configurar_auth(app):
    jwt.init_app(app)