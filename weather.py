import requests
from config import WEATHER_API_KEY

class Weather:
    def __init__(self, city):
        self.city = city.replace(" ", "+") # Replace spaces with '+' for API compatibility
        self.api_key = WEATHER_API_KEY
        self.api_url = f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}"

    def fetch_weather(self):
        """
        Fetches the weather data from the OpenWeatherMap API.
        """
        response = requests.get(self.api_url).json()
        print(response) 
        return response

    def get_temperature(self):
        """
        Retrieves the temperature from the weather data.
        """
        data = self.fetch_weather()
        temperature = round(data["main"]["temp"] - 273.15, 1)  # Convert from Kelvin to Celsius
        return temperature

    def get_description(self):
        """
        Retrieves a brief description of the weather conditions.
        """
        data = self.fetch_weather()
        description = data["weather"][0]["description"]
        return description

weather = Weather("Tel+Aviv")
weather.fetch_weather()