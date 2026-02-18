import requests
import random

URL = "https://restcountries.com/v3.1/all"

def get_random_countries(n=10):
    response = requests.get(URL)
    data = response.json()
    return random.sample(data, n)
