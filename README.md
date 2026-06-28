# Weather Outfit Advisor

A simple Python desktop application that gives outfit recommendations based on the current weather in a selected city.

The project was built using Python, Tkinter, OOP, API requests, geocoding, and a multi-file project architecture.

---

## Features

* Search weather by city name
* Convert city names into latitude and longitude using a geocoding API
* Fetch current weather data from an external weather API
* Display current temperature
* Display current wind speed
* Interpret weather condition codes
* Give outfit recommendations based on temperature
* Add a wind warning when wind speed is high
* Handle empty city input
* Handle invalid city names or API errors
* Use a Tkinter graphical user interface
* Separate the project into multiple Python files using OOP

---

## What I practiced

* Working with APIs using `requests`
* Sending API parameters with `params`
* Using `response.raise_for_status()`
* Converting API responses with `response.json()`
* Extracting nested JSON data
* Using geocoding to convert a city name into coordinates
* Creating custom classes with OOP
* Passing objects from one class to another
* Separating project responsibilities across multiple files
* Building a Tkinter user interface
* Using `Label`, `Entry`, and `Button` widgets
* Connecting a Tkinter button to a custom method
* Updating UI text dynamically with `.config()`
* Handling errors with `try / except`
* Structuring a Python project more professionally

---

## Project structure

 ```‚
main.py
ui.py
geocoding_api.py
weather_api.py
weather_model.py
outfit_advisor.py
``` 

---

## How the project works

The user enters a city name in the Tkinter interface.

The application then uses the geocoding API to convert the city name into latitude and longitude.

Those coordinates are sent to the weather API.

The weather API returns current weather data.

The `Weather` class extracts the useful weather information from the raw API data.

The `OutfitAdvisor` class uses that weather object to generate an outfit recommendation.

The result is displayed in the Tkinter interface.

---

## Application flow

```
User enters city
↓
geocoding_api.py gets latitude and longitude
↓
weather_api.py gets current weather data
↓
weather_model.py creates a Weather object
↓
outfit_advisor.py creates a recommendation
↓
ui.py displays the result
```

---

## How to run

Run the project with:

```bash
python main.py
```

---

## Technologies used

* Python
* Tkinter
* Requests
* Open-Meteo Weather API
* Open-Meteo Geocoding API
* Object-Oriented Programming
* API requests
* JSON

---

## Note

This project was created as part of my Python learning journey through Angela Yu’s Udemy course.

It was built independently, outside the course curriculum, as extra practice to repeat and strengthen the concepts I have learned so far, especially APIs, OOP, Tkinter, and multi-file project structure.

---

## Author

Alex — Aspiring Python developer building projects step by step through daily practice, with the long-term goal of becoming a professional software developer.
