from weather_api import get_weather_data
from weather_model import Weather
from outfit_advisor import OutfitAdvisor

#https://www.latlong.net/

latitude = float(input('Latitude: '))
longitude = float(input('Longitude: '))

data = get_weather_data(latitude, longitude)
weather = Weather(data)
advisor = OutfitAdvisor(weather)

print(f'\n- Temperature: {weather.temperature}°C')
print(f'- Wind speed: {weather.wind_speed} km/h')
print(f'- Recommendation: {advisor.get_recommendation()}')
