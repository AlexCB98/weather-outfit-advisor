class OutfitAdvisor:

    def __init__(self, weather):
        self.weather = weather

    def get_recommendation(self):
        temperature = self.weather.temperature

        if temperature < 5:
            return 'Wear a winter jacket.'
        elif temperature <= 15:
            return 'Wear a jacket.'
        elif temperature <= 22:
            return 'Wear a hoodie or light jacket.'
        else:
            return 'Wear a t-shirt'