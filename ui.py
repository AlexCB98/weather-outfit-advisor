from geocoding_api import get_coordinates
from weather_api import get_weather_data
from weather_model import Weather
from outfit_advisor import OutfitAdvisor
import tkinter as tk

FONT = ('Arial', 20, 'italic')

# Color Hunt palette: https://colorhunt.co/palette/0b1d51725cad8ccdebffe3a9
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
        pass
