import csv
import json
import openpyxl
import os
from webscraper.database_handler import Opinion


def download(file_type, productid):
    opinions = Opinion.query.filter_by(productid=productid).all()
    if productid == '':
        productid = "product"
    
    try:
        print(file_type, productid)
        if file_type == "csv":
            return generate_csv(opinions, productid)
        elif file_type == "json":
            return generate_json(opinions, productid)
        elif file_type == "xlsx":
            return generate_xlsx(opinions, productid)
        else:
            raise Exception("invalid file type")
    except Exception as e:
        print(e)
        return e


def generate_csv(opinions, productid):
    file_path = os.path.join(os.getcwd(), f"{productid}.csv")

    with open(file_path, "w", newline="", encoding="utf-8") as file:
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

    return file_path


def generate_json(opinions, productid):
    file_path = os.path.join(os.getcwd(), f"{productid}.json")

    with open(file_path, "w", encoding="utf-8") as file:
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
        json.dump(products_list, file, ensure_ascii=False, indent=4)

    return file_path


def generate_xlsx(opinions, productid):
    file_path = os.path.join(os.getcwd(), f"{productid}.xlsx")
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

    wb.save(file_path)

    return file_path
