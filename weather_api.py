import requests

def get_weather_data(latitude, longitude):
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True,
    }

    response = requests.get(
        url='https://api.open-meteo.com/v1/forecast',
        params=params,
        timeout=10,
    )
    response.raise_for_status()
    data = response.json()

    return data
