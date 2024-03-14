import random
import requests
import time

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
    
]

def get_random_headers():
    return {
        "User-Agent": random.choice(user_agents),
    }

def get_random_productid():
    random_productid = "".join(random.choices("1234567890", k=random.randint(8, 9)))
    headers = {
        "User-Agent": random.choice(user_agents),
    }
    time.sleep(random.randint(1, 3))
    try:
        print("getting random productid")
        response = requests.get(
            f"https://www.ceneo.pl/{random_productid}", allow_redirects=False, headers=headers
        )
        print(response.status_code)
        response.raise_for_status()
        if response.status_code == 301 or response.status_code == 302:
            raise requests.exceptions.RequestException
    except requests.exceptions.RequestException as e:
        print("RequestException")
        return get_random_productid()

    print("Success")
    print("returning random productid: %s" % random_productid)
    return random_productid if response.status_code == 200 else get_random_productid()
