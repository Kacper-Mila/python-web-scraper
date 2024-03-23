from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///products.db"
db = SQLAlchemy(app)
import webscraper.routes
import webscraper.database_handler
import webscraper.scraper
import webscraper.download_product
import webscraper.sort_opinions
import webscraper.charts_data
