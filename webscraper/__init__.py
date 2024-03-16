from flask import Flask

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///products.db"
import webscraper.routes
import webscraper.database_handler
import webscraper.scraper
import webscraper.download_product
import webscraper.sort_opinions
import webscraper.charts_data
