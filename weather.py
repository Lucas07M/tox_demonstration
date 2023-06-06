import requests

def get_weather(city):
    url = f"https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q={city}"
    response = requests.get(url)
    data = response.json()
    return data["current"]["temp_c"]