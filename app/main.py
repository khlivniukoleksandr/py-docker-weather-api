import os
from dotenv import load_dotenv
import requests

load_dotenv()

API_KEY = os.getenv("API_KEY")

CITY = "Paris"
BASE_URL = f"http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": CITY,
        "lang": "en"
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        location = data["location"]["name"]
        temperature = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        print(f"Weather in {location}: {temperature}°C, {condition}")
    else:
        print("An error occurred, unable to retrieve data")



if __name__ == "__main__":
    get_weather()
