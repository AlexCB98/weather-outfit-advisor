class Weather:

    def __init__(self, data):
        current_weather = data["current_weather"]

        self.temperature = current_weather['temperature']
        self.wind_speed = current_weather['windspeed']
        self.weather_code = current_weather['weathercode']
        self.rain = 0