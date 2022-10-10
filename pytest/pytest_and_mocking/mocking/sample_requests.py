import requests


def get_res():
    print("Making request...")
    res = requests.get("https://www.google.com/")
    return res.status_code
