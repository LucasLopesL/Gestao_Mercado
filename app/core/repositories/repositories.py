from app.core.models.models import db, Seller, Product, Sale

def criar_seller(data):
    seller = Seller(
        nome=data['nome'],
        cnpj=data['cnpj'],
        email=data['email'],
        celular=data['celular'],
        senha=data['senha'],
    )
    db.session.add(seller)
    db.session.commit()
    return seller

def criar_produto(data, seller_id):
    produto = Product(
        nome=data['nome'],
        preco=data['preco'],
        quantidade=data['quantidade'],
        status=data['status'],
        img=data['img'],
        seller_id=seller_id,
    )
    db.session.add(produto)
    db.session.commit()
    return produto
