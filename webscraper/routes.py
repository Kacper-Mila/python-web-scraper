from webscraper import app, scraper, download_product
from flask import render_template, request, send_file


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/product", methods=["GET"])
def product():
    args = request.args
    productid = args.get("productid")
    product = scraper.scrape(productid)

    if isinstance(product, Exception) or product is None:
        return render_template("error.html")

    for opinion in product.product_opinions:
        if opinion.pros is not None:
            opinion.pros = list(filter(None, opinion.pros.split(", ")))
            opinion.cons = list(filter(None, opinion.cons.split(", ")))

    return render_template("product-page.html", product=product)


@app.route("/download", methods=["GET"])
def download():
    args = request.args
    file_type = args.get("type")
    productid = args.get("productid")
    file = download_product.download(file_type, productid)
    
    if file is None:
        return render_template("error.html")
    
    return send_file(file, as_attachment=True)