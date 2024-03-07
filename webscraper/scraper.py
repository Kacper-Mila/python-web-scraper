from bs4 import BeautifulSoup
import requests
from webscraper import database_handler


def scrape(productid: str):
    url: str = f"https://www.ceneo.pl/{productid}"

    if productid == "":
        return Exception("Product not found")
    
    response = requests.get(url)

    if response.status_code != 200:
        return Exception("Product not found")

    soup = BeautifulSoup(response.text, "html.parser")

    product_opinins = soup.find_all(
        "div", class_="user-post user-post__card js_product-review"
    )

    try:
        product_name = soup.find(
            "h1", class_="product-top__product-info__name"
        ).text.strip()
    except:
        product_name = None

    try:
        img_url = soup.find("img", class_="gallery-carousel__media")["src"]
    except:
        img_url = None

    try:
        rating = soup.find("div", class_="score-extend")
        rating = rating.find("div", class_="fl")
        rating = rating.find("font").text.strip()

    except:
        rating = None

    product = database_handler.Product(
        productid=productid, product_name=product_name, img_url=img_url, rating=rating
    )
    database_handler.add_product_to_database(product)

    for opinion in product_opinins:
        try:
            author = opinion.find("span", class_="user-post__author-name").text.strip()
        except:
            author = "Anonim"

        try:
            recommendation = opinion.find(
                "span", class_="user-post__author-recomendation"
            ).text.strip()
        except:
            recommendation = None

        try:
            stars = opinion.find("span", class_="user-post__score-count").text.strip()
        except:
            stars = None

        try:
            content = opinion.find("div", class_="user-post__text").text.strip("\n")
        except:
            content = None

        try:
            pros_and_cons = opinion.find("div", class_="review-feature").text.split(
                "\n"
            )

            pros_and_cons = split_pros_and_cons(pros_and_cons)

            pros = ', '.join(pros_and_cons[0])
            cons = ', '.join(pros_and_cons[1])
        except:
            pros = None
            cons = None

        opinion = database_handler.Opinion(
            author=author,
            recommendation=recommendation,
            stars=stars,
            content=content,
            pros=pros,
            cons=cons,
            productid=product.productid,
        )
        database_handler.add_opinion_to_database(opinion)

    database_handler.commit_to_database()
    print(database_handler.Product.query.get(productid))
    
    return database_handler.Product.query.get(productid)


def split_pros_and_cons(pros_and_cons):
    pros = []
    cons = []
    is_prons = False
    for i in range(len(pros_and_cons)):
        if pros_and_cons[i] == "Zalety":
            is_prons = True

        if pros_and_cons[i] == "Wady":
            is_prons = False

        if is_prons and pros_and_cons[i] != "Zalety":
            pros.append(pros_and_cons[i])
        elif not is_prons and pros_and_cons[i] != "Wady":
            cons.append(pros_and_cons[i])
        else:
            pass

    while "" in pros:
        pros.remove("")
    while "" in cons:
        cons.remove("")

    return [pros, cons]
