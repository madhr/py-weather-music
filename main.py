from weather_to_music_converter import WeatherToMusicConverter

if __name__ == '__main__':

	wtmc = WeatherToMusicConverter()

	api_key = '7f1f66212a27b1173d1c96f3f644b3a5'
	city = 'brisbane,au'

	wtmc.weather_to_music(api_key, city)
