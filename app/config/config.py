class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:rootpassword@db/gestao_estoque'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'supersecreta'
    JWT_SECRET_KEY = 'segredo'  # Usado para assinar o JWT
