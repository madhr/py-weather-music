import requests

from weather_forecast import WeatherTimestamp, Temperature, Pressure, Weather, WeatherForecast


class WeatherApi:

	def get_json_weather_forecast_from_api(self, city, api_key):
		response = requests.get("https://api.openweathermap.org/data/2.5/forecast?q="+city+"&APPID=" + api_key)

		if response.status_code == 200:
			return response.json()
		else:
			return None

	def parse_weather_forecast(self, json_data):
		weather_timestamps = []

		for i in range(len(json_data.get('list'))):
			list_item = json_data.get('list')[i]

			temp = list_item.get('main').get('temp')
			temp_max = list_item.get('main').get('temp_max')
			temp_min = list_item.get('main').get('temp_min')
			feels_like = list_item.get('main').get('feels_like')

			temperature = Temperature(temp, temp_max, temp_min, feels_like)

			sea_level = list_item.get('main').get('sea_level')
			grnd_level = list_item.get('main').get('grnd_level')

			pressure = Pressure(sea_level, grnd_level)

			humidity = list_item.get('main').get('humidity')
			clouds = list_item.get('clouds').get('all')
			wind_speed = list_item.get('wind').get('speed')
			rain = list_item.get('rain', {}).get('3h', None)

			weather = Weather(humidity, clouds, wind_speed, rain)

			timestamp = list_item.get('dt')

			weather_timestamp = WeatherTimestamp(temperature, pressure, weather, timestamp)

			weather_timestamps.append(weather_timestamp)

		city = json_data.get('city').get('name')
		country = json_data.get('city').get('country')
		population = json_data.get('city').get('population')
		sunrise = json_data.get('city').get('sunrise')
		sunset = json_data.get('city').get('sunset')

		weather_forecast = WeatherForecast(city, country, population, sunrise, sunset, weather_timestamps)

		print(weather_forecast)

		return weather_forecast
