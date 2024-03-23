# from webscraper import database_handler
from webscraper.dbmodels import OpinionModel
import json


def get_charts_data(productid):
    data = {
        "recommendations": {
            "labels": ["Polecam", "Nie polecam", "Brak rekomendacji"],
            "datasets": [
                {
                    "label": "Recommendations",
                    "data": [
                        OpinionModel.get_recommendation_count(productid, "Polecam"),
                        OpinionModel.get_recommendation_count(productid, "Nie polecam"),
                        OpinionModel.get_recommendation_count(productid, None),
                    ],
                    "borderColor": "#e5eaf5",
                    "backgroundColor": [
                        "rgba(0, 255, 0, 0.5)",
                        "rgba(255, 0, 0, 0.5)",
                        "rgba(0, 0, 255, 0.5)",
                    ],
                },
            ],
        },
        "stars": {
            "labels": ["1", "2", "3", "4", "5"],
            "datasets": [
                {
                    "label": "Stars count",
                    "data": [
                        OpinionModel.get_stars_count(productid, "1/5", "0,5/5"),
                        OpinionModel.get_stars_count(productid, "2/5", "1,5/5"),
                        OpinionModel.get_stars_count(productid, "3/5", "2,5/5"),
                        OpinionModel.get_stars_count(productid, "4/5", "3,5/5"),
                        OpinionModel.get_stars_count(productid, "5/5", "4,5/5"),
                    ],
                    "borderColor": "#e5eaf5",
                    "backgroundColor": [
                        "rgba(255, 99, 132, 0.5)",
                        "rgba(54, 162, 235, 0.5)",
                        "rgba(255, 206, 86, 0.5)",
                        "rgba(75, 192, 192, 0.5)",
                        "rgba(153, 102, 255, 0.5)",
                    ],
                },
            ],
        },
    }

    json_data = json.dumps(data)
    return json_data
