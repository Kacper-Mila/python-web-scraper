from webscraper import app
from flask_alchemy import SQLAlchemy 

db = SQLAlchemy(app)

class Product_opinion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product = db.Column(db.String(100))
    author = db.Column(db.String(100))
    recommendation = db.Column(db.String(100))
    stars = db.Column(db.String(100))
    content = db.Column(db.String(100))
    pros = db.Column(db.String(100))
    cons = db.Column(db.String(100))

    def __repr__(self):
        return f"Product_opinion('{self.product}', '{self.author}', '{self.recommendation}', '{self.stars}', '{self.content}', '{self.pros}', '{self.cons}')"