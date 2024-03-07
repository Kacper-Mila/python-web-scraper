from webscraper import app, scraper
from flask import render_template, request


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/product", methods=["GET"])
def product():
    args = request.args
    productid = args.get("productid")
    print(f"args: {args} productid: {productid}")
    product = scraper.scrape(productid)

    if isinstance(product, Exception):
        return render_template("error.html")
    
    for opinion in product.product_opinions:
        if opinion.pros is not None:
            opinion.pros = opinion.pros.split(", ")
            opinion.cons = opinion.cons.split(", ")
    
    return render_template(
        "product-page.html", product=product
    )