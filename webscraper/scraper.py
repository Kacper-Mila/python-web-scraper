from bs4 import BeautifulSoup
import requests
from datetime import datetime
from webscraper import database_handler, utils


def scrape(productid):
    url: str = f"https://www.ceneo.pl/{productid}"
    headers = utils.get_random_headers()

    if not productid:
        return Exception("Product ID cannot be empty")

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return Exception(f"Product with ID: {productid} not found")

    soup = BeautifulSoup(response.text, "html.parser")

    product_name = scrape_product_name(soup)
    img_url = scrape_img_url(soup)
    rating = scrape_rating(soup)

    product = database_handler.Product(
        productid=productid, product_name=product_name, img_url=img_url, rating=rating
    )
    database_handler.add_product_to_database(product)

    scrape_all_product_opinions(url, productid)

    database_handler.commit_to_database()

    return database_handler.Product.query.get(productid)


def scrape_product_name(soup):
    try:
        return soup.find("h1", class_="product-top__product-info__name").text.strip()
    except:
        return None


def scrape_img_url(soup):
    try:
        return soup.find("img", class_="gallery-carousel__media")["src"]
    except:
        return None


def scrape_rating(soup):
    try:
        rating = soup.find("div", class_="score-extend")
        rating = rating.find("div", class_="fl")
        return rating.find("font").text.strip()
    except:
        return None


def scrape_all_product_opinions(url, productid, pros_count=0, cons_count=0):
    product_opinions = []
    soup2 = BeautifulSoup(requests.get(url, allow_redirects=False).text, "html.parser")
    product_opinions.extend(
        soup2.find_all("div", class_="user-post user-post__card js_product-review")
    )

    for i in range(2, 5):
        try:
            response2 = requests.get(f"{url}/opinie-{i}", allow_redirects=False)
            soup2 = BeautifulSoup(response2.text, "html.parser")
            product_opinions.extend(
                soup2.find_all(
                    "div", class_="user-post user-post__card js_product-review"
                )
            )
        except:
            break

    database_handler.get_product(productid).opinions_count = len(product_opinions)

    for opinion in product_opinions:
        opinion_id = scrape_opionion_id(opinion)
        author = scrape_opinion_author(opinion)
        recommendation = scrape_opinion_recommendation(opinion)
        stars = scrape_opinion_stars(opinion)
        confirmed_purchase = scrape_opinion_confirmed_purchase(opinion)
        opinion_date = scrape_opinion_date(opinion)
        buy_date = scrape_opinion_date(opinion)
        content = scrape_opinion_content(opinion)
        helpfull = scrape_helpfull_button(opinion)
        not_helpfull = scrape_not_helpfull_button(opinion)
        
        try:
            pros_and_cons = opinion.find("div", class_="review-feature").text.split(
                "\n"
            )

            pros_and_cons = split_pros_and_cons(pros_and_cons)

            pros_count += len(pros_and_cons[0])
            cons_count += len(pros_and_cons[1])

            pros = ", ".join(pros_and_cons[0])
            cons = ", ".join(pros_and_cons[1])
        except:
            pros = None
            cons = None

        opinion = database_handler.Opinion(
            id=opinion_id,
            author=author,
            recommendation=recommendation,
            stars=stars,
            confirmed_purchase=confirmed_purchase,
            date_of_opinion=opinion_date,
            buy_date=buy_date,
            content=content,
            pros=pros,
            cons=cons,
            helpfull=helpfull,
            not_helpfull=not_helpfull,
            productid=productid,
        )
        database_handler.add_opinion_to_database(opinion)

    database_handler.get_product(productid).total_pros_count = pros_count
    database_handler.get_product(productid).total_cons_count = cons_count


def scrape_opionion_id(opinion):
    try:
        opinion_id = opinion.get("data-entry-id")
    except:
        opinion_id = None

    return opinion_id


def scrape_opinion_author(opinion):
    try:
        author = opinion.find("span", class_="user-post__author-name").text.strip()
    except:
        author = "Anonim"

    return author


def scrape_opinion_recommendation(opinion):
    try:
        recommendation = opinion.find(
            "span", class_="user-post__author-recomendation"
        ).text.strip()
    except:
        recommendation = None

    return recommendation


def scrape_opinion_stars(opinion):
    try:
        stars = opinion.find("span", class_="user-post__score-count").text.strip()
    except:
        stars = None

    return stars


def scrape_opinion_confirmed_purchase(opinion):
    try:
        confirmed_purchase_div = opinion.find("div", class_="review-pz")
        if confirmed_purchase_div is not None:
            confirmed_purchase = True
        else:
            confirmed_purchase = False
    except:
        confirmed_purchase = None
        
    return confirmed_purchase


def scrape_opinion_date(opinion):
    date_span = opinion.find("span", class_="user-post__published")
    date_strings = date_span.find_all("time")
    try:
        opinion_date_string = date_strings[0].get("datetime")
        opinion_date = datetime.strptime(opinion_date_string, "%Y-%m-%d %H:%M:%S")
    except:
        opinion_date = None

    return opinion_date


def scrape_opinion_buy_date(opinion):
    date_span = opinion.find("span", class_="user-post__published")
    date_strings = date_span.find_all("time")
    try:
        buy_date_string = date_strings[1].get("datetime")
        buy_date = datetime.strptime(buy_date_string, "%Y-%m-%d %H:%M:%S")
    except:
        buy_date = None

    return buy_date


def scrape_opinion_content(opinion):
    try:
        content = opinion.find("div", class_="user-post__text").text.strip("\n")
    except:
        content = None

    return content


def scrape_helpfull_button(opinion):
    try:
        helpfull_button = opinion.find(
            "button", class_="vote-yes js_product-review-vote js_vote-yes"
        )
        helpfull = int(helpfull_button.find("span").text)
    except:
        helpfull = 0

    return helpfull

def scrape_not_helpfull_button(opinion):
    try:
        not_helpfull_button = opinion.find(
            "button", class_="vote-no js_product-review-vote js_vote-no"
        )
        not_helpfull = int(not_helpfull_button.find("span").text)
    except:
        not_helpfull = 0
        
    return not_helpfull

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
