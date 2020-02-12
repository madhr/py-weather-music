from unittest import TestCase

from weather.weather_api import WeatherApi
from weather.weather_forecast import WeatherForecast


class TestWeatherApi(TestCase):
    weather_api = WeatherApi()

    def test_get_weather_forecast_from_api(self):
        api_key = '7f1f66212a27b1173d1c96f3f644b3a5'
        city = 'london,uk'
        forecast = self.weather_api.get_weather_forecast_from_api(city, api_key)
        self.assertIsInstance(forecast, WeatherForecast)
        self.assertEqual(len(forecast.weather_timestamps), 40)
        self.assertGreaterEqual(forecast.weather_timestamps[0].temperature.feels_like, 0)
        self.assertGreaterEqual(forecast.weather_timestamps[0].temperature.temp_max, 0)
        self.assertGreaterEqual(forecast.weather_timestamps[0].temperature.temp_min, 0)
        self.assertGreaterEqual(forecast.weather_timestamps[0].weather.clouds, 0)
        self.assertGreaterEqual(forecast.weather_timestamps[0].weather.humidity, 0)
        self.assertGreaterEqual(forecast.weather_timestamps[0].weather.wind_speed, 0)
        self.assertGreaterEqual(forecast.weather_timestamps[0].weather.rain, 0)

