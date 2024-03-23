from webscraper import app, db

class Product(db.Model):
    productid = db.Column(db.String(100), primary_key=True)
    product_name = db.Column(db.String(100))
    img_url = db.Column(db.String(100))
    rating = db.Column(db.String(100))
    opinions_count = db.Column(db.Integer, default=0)
    total_pros_count = db.Column(db.Integer, default=0)
    total_cons_count = db.Column(db.Integer, default=0)
    product_opinions = db.relationship("Opinion", backref="product", lazy=True)

    def __repr__(self) -> str:
        return "<Product %r>" % self.product_name
    
    def __str__(self) -> str:
        return (
            f"\nProduct: \n"
            f"productid: {self.productid}, \n"
            f"product_name: {self.product_name}, \n"
            f"img_url: {self.img_url}, \n"
            f"rating: {self.rating}, \n"
            f"opinions_count: {self.opinions_count}, \n"
            f"total_pros_count: {self.total_pros_count}, \n"
            f"total_cons_count: {self.total_cons_count}, \n"
            f"product_opinions: {self.product_opinions}"
        )
        
with app.app_context():
    db.create_all()
    
    
def add_to_db(product: Product):
    try:
        db.session.add(product)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return f"Error adding product to database: {e}"
    
def remove_from_db(product: Product):
    try:
        db.session.delete(product)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return f"Error removing product from database: {e}"
    
def get_by_id(productid: str) -> Product:
    try:
        return Product.query.get(productid)
    except Exception as e:
        return f"Error getting product with ID {productid}: {e}"
    
def get_all() -> list[Product]:
    try:
        return Product.query.all()
    except Exception as e:
        return f"Error getting all products: {e}"