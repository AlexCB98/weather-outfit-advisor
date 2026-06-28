class OutfitAdvisor:

    def __init__(self, weather):
        self.weather = weather

    def get_recommendation(self):
        temperature = self.weather.temperature
        wind_speed = self.weather.wind_speed

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


        return recommendation
