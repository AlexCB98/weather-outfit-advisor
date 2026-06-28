from weather_api import get_weather_data
from weather_model import Weather
from outfit_advisor import OutfitAdvisor

#https://www.latlong.net/

LATITUDE = 48.669102
LONGITUDE = 12.690720

data = get_weather_data(LATITUDE, LONGITUDE)
weather = Weather(data)
advisor = OutfitAdvisor(weather)

print(advisor.get_recommendation())