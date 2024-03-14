import random
import requests


def get_random_productid():
    random_productid = "".join(random.choices("1234567890", k=random.randint(8, 9)))

    try:
        response = requests.get(
            f"https://www.ceneo.pl/{random_productid}", allow_redirects=False
        )
        response.raise_for_status()
        if response.status_code == 301:
            raise requests.exceptions.RequestException
    except requests.exceptions.RequestException as e:
        return get_random_productid()

    return random_productid if response.status_code == 200 else get_random_productid()
