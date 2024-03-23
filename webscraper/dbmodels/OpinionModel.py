from webscraper import app, db
from sqlalchemy import DateTime


class Opinion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100))
    recommendation = db.Column(db.String(100))
    stars = db.Column(db.String(100))
    confirmed_purchase = db.Column(db.Boolean, default=False)
    date_of_opinion = db.Column(DateTime)
    buy_date = db.Column(DateTime)
    content = db.Column(db.String(1000))
    pros = db.Column(db.String(100))
    cons = db.Column(db.String(100))
    helpfull = db.Column(db.Integer, default=0)
    not_helpfull = db.Column(db.Integer, default=0)
    productid = db.Column(
        db.String(100), db.ForeignKey("product.productid"), nullable=False
    )

    def __repr__(self) -> str:
        return "<Opinion %r>" % self.id

    def __str__(self) -> str:
        return (
            f"\nOpinion: \n"
            f"id: {self.id}, \n"
            f"author: {self.author}, \n"
            f"recommendation: {self.recommendation}, \n"
            f"stars: {self.stars}, \n"
            f"confirmed_purchase: {self.confirmed_purchase}, \n"
            f"date_of_opinion: {self.date_of_opinion}, \n"
            f"buy_date: {self.buy_date}, \n"
            f"content: {self.content}, \n"
            f"pros: {self.pros}, \n"
            f"cons: {self.cons}, \n"
            f"helpfull: {self.helpfull}, \n"
            f"not_helpfull: {self.not_helpfull}, \n"
            f"productid: {self.productid}"
        )
    
with app.app_context():
    db.create_all()
    
def add_to_db(opinion: Opinion):
    try:
        db.session.add(opinion)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return f"Error adding opinion to database: {e}"
    
def remove_from_db(opinion: Opinion):
    try:
        db.session.delete(opinion)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return f"Error removing opinion from database: {e}"

def get_by_id(opinionid: int) -> Opinion:
    try:
        return Opinion.query.get(opinionid)
    except Exception as e:
        return f"Error getting opinion with ID {opinionid}: {e}"

def get_by_productid(productid: str) -> list[Opinion]:
    try:
        return Opinion.query.filter_by(productid=productid).all()
    except Exception as e:
        return f"Error getting opinions with product ID {productid}: {e}"
    
def get_all() -> list[Opinion]:
    try:
        return Opinion.query.all()
    except Exception as e:
        return f"Error getting all opinions: {e}"
    
def get_recommendation_count(productid: str, recommendation: str) -> int:
    try:
        return Opinion.query.filter_by(productid=productid, recommendation=recommendation).count()
    except Exception as e:
        return f"Error getting recommendation count for product {productid}: {e}"
    
def get_stars_count(productid: str, stars1: str, stars2: str) -> int:
    try:
        return Opinion.query.filter(
            Opinion.productid == productid, Opinion.stars.in_([stars1, stars2])
        ).count()
    except Exception as e:
        return f"Error getting stars count for product {productid}: {e}"
    
def is_same_opinion(opinion1: Opinion, opinion2: Opinion) -> bool:
    return (
        opinion1.author == opinion2.author
        and opinion1.recommendation == opinion2.recommendation
        and opinion1.stars == opinion2.stars
        and opinion1.confirmed_purchase == opinion2.confirmed_purchase
        and opinion1.date_of_opinion == opinion2.date_of_opinion
        and opinion1.buy_date == opinion2.buy_date
        and opinion1.content == opinion2.content
        and opinion1.pros == opinion2.pros
        and opinion1.cons == opinion2.cons
        and opinion1.helpfull == opinion2.helpfull
        and opinion1.not_helpfull == opinion2.not_helpfull
        and opinion1.productid == opinion2.productid
    )