import tkinter as tk


class WeatherApp:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Weather Outfit Advisor")
        self.window.minsize(width=500, height=500)
        self.window.config(padx=30, pady=30)

        self.window.mainloop()