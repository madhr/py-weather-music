class WeatherForecast:

	def __init__(self, city, country, population, sunrise, sunset, weather_timestamps):
		self.city = city
		self.country = country
		self.population = population
		self.sunrise = sunrise
		self.sunset = sunset
		self.weather_timestamps = weather_timestamps


class WeatherTimestamp:

	def __init__(self, temperature, pressure, weather, timestamp):
		self.temperature = temperature
		self.pressure = pressure
		self.weather = weather
		self.timestamp = timestamp


class Temperature:

	def __init__(self, temp, temp_max, temp_min, feels_like):
		self.temp = temp
		self.temp_max = temp_max
		self.temp_min = temp_min
		self.feels_like = feels_like


class Pressure:

	def __init__(self, sea_level, ground_level):
		self.sea_level = sea_level
		self.ground_level = ground_level


class Weather:

	def __init__(self, humidity, clouds, wind_speed, rain):
		self.humidity = humidity
		self.clouds = clouds
		self.wind_speed = wind_speed
		self.rain = rain

