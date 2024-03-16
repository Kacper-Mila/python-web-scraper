from webscraper import (
    app,
    scraper,
    download_product,
    sort_opinions,
    database_handler,
    utils,
)
from flask import render_template, request, send_file


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/product", methods=["GET"])
def product():
    args = request.args
    sort_by = args.get("sort")
    random = args.get("random")

    if random is not None:
        productid = utils.get_random_productid()
    else:
        productid = args.get("productid")

    database_product = database_handler.get_product(productid)

    if not database_product:
        product = scraper.scrape(productid)
    else:
        product = database_product

    if isinstance(product, Exception) or product is None:
        return render_template("error.html", exception=product)

    for opinion in product.product_opinions:
        if opinion.pros is not None:
            opinion.pros = list(filter(None, opinion.pros.split(", ")))
            opinion.cons = list(filter(None, opinion.cons.split(", ")))

    sort_opinions.sort(product.product_opinions, sort_by)
    return render_template("product-page.html", product=product)


@app.route("/download", methods=["GET"])
def download():
    args = request.args
    file_type = args.get("file_type")
    productid = args.get("productid")
    file = download_product.download(file_type, productid)

    if file is None or isinstance(file, Exception):
        return render_template("error.html", error=file)

    return send_file(file, as_attachment=True)


@app.route("/product-charts", methods=["GET"])
def product_charts():
    args = request.args
    productid = args.get("productid")
    return render_template(
        "product-charts.html",
        productid=productid,
    )


@app.route("/charts-data", methods=["GET"])
def charts_data():
    from webscraper import charts_data

    args = request.args
    productid = args.get("productid")
    data = charts_data.get_charts_data(productid)
    return data


@app.route("/product-list", methods=["GET"])
def product_list():
    products = database_handler.get_all_products()
    products.reverse()
    return render_template("product-list.html", products=products)
