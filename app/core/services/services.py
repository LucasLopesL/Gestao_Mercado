from app.core.models.models import db, Seller, Product
from werkzeug.security import check_password_hash

def validar_login(email, senha):
    seller = Seller.query.filter_by(email=email).first()
    if seller and check_password_hash(seller.senha, senha):
        return seller
    return None

def atualizar_estoque(produto_id, quantidade_vendida):
    produto = Product.query.get(produto_id)
    if produto and produto.quantidade >= quantidade_vendida:
        produto.quantidade -= quantidade_vendida
        db.session.commit()
        return produto
    return None
