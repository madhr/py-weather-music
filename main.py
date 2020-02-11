from weather_to_music_converter import WeatherToMusicConverter
import argparse

API_KEY = '7f1f66212a27b1173d1c96f3f644b3a5'

if __name__ == '__main__':

	parser = argparse.ArgumentParser(description='Pass city name and two digit country code')
	parser.add_argument('city', metavar='city', type=str, nargs=1, help='city name')
	parser.add_argument('country', metavar='country', type=str, nargs=1, help='2 digit country code ISO 3166-1 compliant')

	args = parser.parse_args()

	city = args.city
	country = args.country
	city_and_country = city[0]+','+country[0]

	wtmc = WeatherToMusicConverter()
	wtmc.weather_to_music(API_KEY, city_and_country)
