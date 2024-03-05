from bs4 import BeautifulSoup
import requests


def scrape(productid: str):
    url: str = f"https://www.ceneo.pl/{productid}"
    print(productid)
    
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    
    product_opinins = soup.find_all("div", class_="user-post user-post__card js_product-review")
    product_data = []
    
    for opinion in product_opinins:
        try:
            produc_name = soup.find("h1", class_="product-top__product-info__name").text.strip()
        except:
            produc_name = None
        
        try:
            author = opinion.find("span", class_="user-post__author-name").text.strip()
        except:
            author = "Anonim"
        
        try:
            recommendation = opinion.find("span", class_="user-post__author-recomendation").text.strip()
        except:
            recommendation = None
            
        try:
            stars = opinion.find("span", class_="user-post__score-count").text.strip()
        except:
            stars = None
            
        try:
            content = opinion.find("div", class_="user-post__text").text.strip()
        except:
            content = None
            
        try:
            pros = opinion.find("div", class_="review-feature__col review-feature__col--positives").text.strip()
        except:
            pros = None
            
        try:
            cons = opinion.find("div", class_="review-feature__col review-feature__col--negatives").text.strip()
        except:
            cons = None
            
        opinion_dict = {
            "product": produc_name,
            "author": author,
            "recommendation": recommendation,
            "stars": stars,
            "content": content,
            "pros": pros,
            "cons": cons,
        }
        product_data.append(opinion_dict)
    return product_data