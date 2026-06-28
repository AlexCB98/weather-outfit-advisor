from geocoding_api import get_coordinates
from weather_api import get_weather_data
from weather_model import Weather
from outfit_advisor import OutfitAdvisor


city_name = input("City: ")

location = get_coordinates(city_name)

latitude = location["latitude"]
longitude = location["longitude"]

data = get_weather_data(latitude, longitude)
weather = Weather(data)
advisor = OutfitAdvisor(weather)

print(f'\nCity: {location["name"]}, {location["country"]}')
print(f'- Temperature: {weather.temperature}°C')
print(f'- Wind speed: {weather.wind_speed} km/h')
print(f'- Recommendation: {advisor.get_recommendation()}')