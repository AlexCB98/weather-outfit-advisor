from geocoding_api import get_coordinates
from weather_api import get_weather_data
from weather_model import Weather
from outfit_advisor import OutfitAdvisor
import tkinter as tk

FONT = ('Arial', 20, 'italic')

NAVY = '#0B1D51'
PURPLE = '#725CAD'
SKY_BLUE = '#8CCDEB'
CREAM = '#FFE3A9'

class WeatherApp:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Weather Outfit Advisor")
        self.window.minsize(width=500, height=300)
        self.window.config(padx=30, pady=30, bg=SKY_BLUE)
        self.window.grid_columnconfigure(0, weight=1, uniform='input')
        self.window.grid_columnconfigure(1, weight=1, uniform='input')

        self.label_1 = tk.Label(
            text='Write your city:',
            font=FONT,
            bg=NAVY,
            fg=CREAM,
            padx=10,
            pady=6,
        )
        self.label_1.grid(row=0, column=0, sticky='nsew', padx=(0, 6))

        self.entry = tk.Entry(
            font=FONT,
            bg=CREAM,
            fg=NAVY,
            insertbackground=NAVY,
            relief='flat',
            justify='center',
        )
        self.entry.grid(row=0, column=1, sticky='nsew', padx=(6, 0))

        self.button = tk.Button(
            text='Get recommendation',
            command=self.get_weather_recommendation,
            font=('Arial', 14, 'bold'),
            bg=PURPLE,
            fg='white',
            activebackground=NAVY,
            activeforeground=CREAM,
            relief='flat',
            cursor='hand2',
            padx=18,
            pady=10,
        )
        self.button.grid(row=1, column=0, columnspan=2, pady=50)

        self.label_2 = tk.Label(
            text='Result...',
            font=FONT,
            bg=SKY_BLUE,
            fg=NAVY,
        )
        self.label_2.grid(row=2, column=0, columnspan=2, sticky='ew')

        self.window.mainloop()


    def get_weather_recommendation(self):
        city_name = self.entry.get().title()
        if not city_name:
            self.label_2.config(text='Please enter a city name.')
            return

        try:
            location = get_coordinates(city_name)

            latitude = location["latitude"]
            longitude = location["longitude"]

            data = get_weather_data(latitude, longitude)
            weather = Weather(data)
            advisor = OutfitAdvisor(weather)

            result_text = (
                f'City: {location["name"]}, {location["country"]}\n\n'
                f'Temperature: {weather.temperature}°C\n'
                f'Wind speed: {weather.wind_speed} km/h\n\n'
                f'Recommendation:\n{advisor.get_recommendation()}'
            )

            self.label_2.config(text=result_text)

        except Exception:
            self.label_2.config(text='City not found or API error.')
