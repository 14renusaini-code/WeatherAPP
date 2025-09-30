import json
import requests

API_KEY = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        # Save response to data/sample_response.json
        with open("data/sample_response.json", "w") as f:
            json.dump(data, f, indent=2)
        return data
    else:
        print("City not found or API error.")
        return None
