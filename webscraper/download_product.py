import csv
import json
from webscraper.database_handler import Product, Opinion


def download(file_type, productid):
    if file_type == "csv":
        return generate_csv(productid)
    elif file_type == "json":
        return generate_json(productid)
    elif file_type == "xlsx":
        return generate_xlsx(productid)
    else:
        return None


def generate_csv(productid):
    opinions = Opinion.query.filter_by(productid=productid).all()

    with open("product_opinions.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["author", "recommendaton", "stars", "content", "pros", "cons"])

        for opinion in opinions:
            writer.writerow(
                [
                    opinion.author,
                    opinion.recommendation,
                    opinion.stars,
                    opinion.content,
                    opinion.pros,
                    opinion.cons,
                ]
            )

    return "product_opinions.csv"


def generate_json(productid):
    opinions = Opinion.query.filter_by(productid=productid).all()

    with open("product_opinions.json", "w") as file:
        products_list = []
        for opinion in opinions:
            opinion_dict = {
                "author": opinion.author,
                "recommendation": opinion.recommendation,
                "stars": opinion.stars,
                "content": opinion.content,
                "pros": opinion.pros,
                "cons": opinion.cons,
            }
            products_list.append(opinion_dict)
        json.dump(products_list, file, indent=4)

    return "product_opinions.json"


def generate_xlsx(productid):
    opinions = Opinion.query.filter_by(productid=productid).all()

    import openpyxl

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(["author", "recommendaton", "stars", "content", "pros", "cons"])

    for opinion in opinions:
        ws.append(
            [
                opinion.author,
                opinion.recommendation,
                opinion.stars,
                opinion.content,
                opinion.pros,
                opinion.cons,
            ]
        )

    wb.save("products.xlsx")

    return "products.xlsx"
