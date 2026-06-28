import requests

def get_coordinates(city_name):
    params = {
        "name": city_name,
        "count": 1,
        "language": "en",
        "format": "json",
    }

    response = requests.get(
        url="https://geocoding-api.open-meteo.com/v1/search",
        params=params,
        timeout=10,
    )
    response.raise_for_status()
    data = response.json()

    location = data['results'][0]

    return location
