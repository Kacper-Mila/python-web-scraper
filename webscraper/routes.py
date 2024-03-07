from webscraper import app, scraper, download_product, sort_opinions
from flask import render_template, request, send_file


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/product", methods=["GET"])
def product():
    args = request.args
    productid = args.get("productid")
    sort_by = args.get("sort")
    product = scraper.scrape(productid)

    if isinstance(product, Exception) or product is None:
        return render_template("error.html")

    for opinion in product.product_opinions:
        if opinion.pros is not None:
            opinion.pros = list(filter(None, opinion.pros.split(", ")))
            opinion.cons = list(filter(None, opinion.cons.split(", ")))
    
    sort_opinions.sort(product.product_opinions, sort_by)

    return render_template("product-page.html", product=product)


@app.route("/download", methods=["GET"])
def download():
    args = request.args
    print("download args")
    print(args)
    file_type = args.get("file_type")
    print("file type")
    print(file_type)
    productid = args.get("productid")
    file = download_product.download(file_type, productid)
    
    if file is None or isinstance(file, Exception):
        return render_template("error.html", error=file)
    
    return send_file(file, as_attachment=True)