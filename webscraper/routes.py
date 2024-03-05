from webscraper import app, scraper
from flask import render_template, request


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/scrape", methods=["GET"])
def scrape():
    args = request.args
    productid = args.get("productid")
    print(f"args: {args} productid: {productid}")
    product_data = scraper.scrape(productid)
    return render_template("scrape.html", product_data=product_data, productid=productid)