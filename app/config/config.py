import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://user:password@localhost/gestao_estoque'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)  # para JWT
