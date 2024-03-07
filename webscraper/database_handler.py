from webscraper import app
from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy(app)

class Product(db.Model):
    productid = db.Column(db.String(100), primary_key=True)
    product_name = db.Column(db.String(100))
    img_url = db.Column(db.String(100))
    rating = db.Column(db.String(100))
    product_opinions = db.relationship("Opinion", backref="product", lazy=True)
    
    def __repr__(self) -> str:
        return '<Product %r>' % self.product_name


class Opinion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100))
    recommendation = db.Column(db.String(100))
    stars = db.Column(db.String(100))
    content = db.Column(db.String(1000))
    pros = db.Column(db.String(100))
    cons = db.Column(db.String(100))
    productid = db.Column(db.String(100), db.ForeignKey("product.productid"), nullable=False)
    
    def __repr__(self) -> str:
        return '<Opinion %r>' % self.id

    
with app.app_context():
    db.create_all()
    

def add_product_to_database(product: Product):
    try:
        db.session.add(product)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()

def add_opinion_to_database(opinion: Opinion):
    try:
        db.session.add(opinion)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
    
def commit_to_database():
    db.session.commit()
    
def remove_product_from_database(productid: str):
    product = Product.query.get(productid)
    if product is not None:
        db.session.delete(product)
        db.session.commit()