from flask import Flask
from app.adapters.api import routes
import pymysql
from flask_sqlalchemy import SQLAlchemy

pymysql.install_as_MySQLdb()

db = SQLAlchemy()

def criar_app():
    app = Flask(__name__, template_folder="app\web\templates\index.html")
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:senha@localhost/gestao_estoque'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app
