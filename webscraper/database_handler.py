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
        return "<Product %r>" % self.product_name


class Opinion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100))
    recommendation = db.Column(db.String(100))
    stars = db.Column(db.String(100))
    content = db.Column(db.String(1000))
    pros = db.Column(db.String(100))
    cons = db.Column(db.String(100))
    productid = db.Column(
        db.String(100), db.ForeignKey("product.productid"), nullable=False
    )

    def __repr__(self) -> str:
        return "<Opinion %r>" % self.id

    def __str__(self) -> str:
        return (
            f"id: {self.id}, \n"
            f"author: {self.author}, \n"
            f"recommendation: {self.recommendation}, \n"
            f"stars: {self.stars}, \n"
            f"content: {self.content}, \n"
            f"pros: {self.pros}, \n"
            f"cons: {self.cons}, \n"
            f"productid: {self.productid}"
        )


with app.app_context():
    db.create_all()


def add_product_to_database(product: Product):
    existing_product = Product.query.get(product.productid)
    if existing_product is not None:
        existing_product.product_name = product.product_name
        existing_product.img_url = product.img_url
        existing_product.rating = product.rating
    else:
        try:
            db.session.add(product)
        except Exception as e:
            print(e)
            db.session.rollback()


def add_opinion_to_database(opinion: Opinion):
    existing_opinions = Opinion.query.filter_by(productid=opinion.productid).all()

    for ex_opinion in existing_opinions:
        if is_same_opinion(ex_opinion, opinion):
            return

    try:
        db.session.add(opinion)
    except Exception as e:
        print(e)
        db.session.rollback()


def commit_to_database():
    try:
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()


def remove_product_from_database(productid: str):
    product = Product.query.get(productid)
    if product is not None:
        db.session.delete(product)
        db.session.commit()


def get_product(productid: str) -> Product:
    return Product.query.get(productid)

def get_opinion_recommendation_count(productid: str, recommendation: str) -> int:
    return Opinion.query.filter_by(productid=productid, recommendation=recommendation).count()

def get_opinion_stars_count(productid: str, stars: int) -> int:
    return Opinion.query.filter_by(productid=productid, stars=stars).count()

def is_same_opinion(opinion1: Opinion, opinion2: Opinion) -> bool:
    return (
        opinion1.author == opinion2.author
        and opinion1.recommendation == opinion2.recommendation
        and opinion1.stars == opinion2.stars
        and opinion1.content == opinion2.content
        and opinion1.pros == opinion2.pros
        and opinion1.cons == opinion2.cons
    )
