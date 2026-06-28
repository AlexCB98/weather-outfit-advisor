class OutfitAdvisor:

    def __init__(self, weather):
        self.weather = weather

    def get_recommendation(self):
        temperature = self.weather.temperature
        wind_speed = self.weather.wind_speed
        weather_code = self.weather.weather_code

        if temperature < 5:
            recommendation = 'Wear a winter jacket.'
        elif temperature <= 15:
            recommendation = 'Wear a jacket.'
        elif temperature <= 22:
            recommendation = 'Wear a hoodie or light jacket.'
        else:
            recommendation = 'Wear a t-shirt.'

        if wind_speed > 25:
            recommendation += '\nIt is windy outside.'

        if weather_code == 0:
            recommendation += '\nWeather: Clear sky.'
        elif weather_code == 1:
            recommendation += '\nWeather: Mainly clear.'
        elif weather_code == 2:
            recommendation += '\nWeather: Partly cloudy.'
        elif weather_code == 3:
            recommendation += '\nWeather: Overcast.'
        elif weather_code in [45, 48]:
            recommendation += '\nWeather: Fog.'
        elif weather_code in [51, 53, 55]:
            recommendation += '\nWeather: Drizzle.'
        elif weather_code in [61, 63, 65]:
            recommendation += '\nWeather: Rain.'
        elif weather_code in [71, 73, 75]:
            recommendation += '\nWeather: Snow.'
        elif weather_code == 95:
            recommendation += '\nWeather: Thunderstorm.'
        else:
            recommendation += '\nWeather: Unknown weather condition.'


        return recommendation
