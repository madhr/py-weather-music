from pathlib import Path

from mido import MidiFile, MidiTrack

from appenders.wind_appender import WindAppender
from appenders.clouds_appender import CloudsAppender
from appenders.humidity_appender import HumidityAppender
from appenders.rain_appender import RainAppender
from appenders.temperature_appender import TemperatureAppender
from util.converters import Converter
from melody_builder import MelodyBuilder
from sequences.wind_sequence import WindSequence
from sequences.clouds_sequence import CloudsSequence
from sequences.humidity_sequence import HumiditySequence
from sequences.rain_sequence import RainSequence
from sequences.temperature_sequence import TemperatureSequence
from util.instruments import Instruments
from util.music_scale import MusicScale
from tracks.temperature_track import TemperatureTrack
from tracks.clouds_track import CloudsTrack
from tracks.humidity_track import HumidityTrack
from tracks.rain_track import RainTrack
from tracks.wind_track import WindTrack
from weather_api.weather_api import WeatherApi


class WeatherToMusicConverter:

	TICKS_PER_BEAT = 400
	PHRASE_LENGTH = 1200
	OUTPUT_FILE_DIR = 'midi_out'
	converter = Converter()
	music_scales = MusicScale()

	def weather_to_music(self, api_key, city):
		api_handling = WeatherApi()

		weather_forecast = api_handling.get_weather_forecast_from_api(city, api_key)

		outfile = MidiFile()
		outfile.ticks_per_beat = self.TICKS_PER_BEAT

		melody_builder = MelodyBuilder(outfile, self.PHRASE_LENGTH)

		temperature = TemperatureTrack(1, Instruments.BrightAcousticPiano)
		rain = RainTrack(2, Instruments.Celesta)
		clouds = CloudsTrack(3, Instruments.TremoloStrings)
		humidity = HumidityTrack(4, Instruments.ElectricGuitar_clean)
		wind = WindTrack(5, Instruments.Seashore)

		for track in [temperature, rain, clouds, humidity, wind]:
			melody_builder.set_instrument(track.get_track(), track.get_channel(), track.get_instrument())

		for entry in weather_forecast.weather_timestamps:

			base_note = self.converter.temperature_to_base_note(entry.temperature.feels_like)
			music_scale = self.music_scales.melodic_minor(base_note)

			temperature_sequence = TemperatureSequence(entry.temperature, self.PHRASE_LENGTH, base_note, temperature.get_track())
			temperature_appender = TemperatureAppender()
			temperature_appender.append(melody_builder, temperature_sequence, temperature)

			rain_sequence = RainSequence(entry.weather.rain, self.PHRASE_LENGTH, base_note, rain.get_track(), music_scale)
			rain_appender = RainAppender()
			rain_appender.append(melody_builder, rain_sequence, rain)

			clouds_sequence = CloudsSequence(entry.weather.clouds, self.PHRASE_LENGTH, base_note, clouds.get_track())
			clouds_appender = CloudsAppender()
			clouds_appender.append(melody_builder, clouds_sequence, clouds)

			humidity_sequence = HumiditySequence(entry.weather.humidity, self.PHRASE_LENGTH, base_note, humidity.get_track())
			humidity_appender = HumidityAppender()
			humidity_appender.append(melody_builder, humidity_sequence, humidity)

			wind_sequence = WindSequence(entry.weather.wind_speed, self.PHRASE_LENGTH, base_note, wind.get_track())
			wind_appender = WindAppender()
			wind_appender.append(melody_builder, wind_sequence, wind)

		for track in [temperature.get_track(), rain.get_track(), clouds.get_track(), humidity.get_track(), wind.get_track()]:
			outfile.tracks.append(track)

		file_name = 'weather_song_' + weather_forecast.city + '_' + weather_forecast.country + '_' + str(weather_forecast.weather_timestamps[0].timestamp)
		self.save_file(outfile, self.OUTPUT_FILE_DIR, file_name)

	def save_file(self, outfile: MidiFile, file_dir: str, file_name: str) -> MidiFile:
		Path(file_dir).mkdir(exist_ok=True)
		outfile.save(file_dir + '/' + file_name + '.mid')
		print("file saved at " + file_dir + '/' + file_name + '.mid')
		return outfile

	def get_midi_track_time(self, midi_track: MidiTrack):
		sum = 0
		for message in midi_track:
			sum += message.time
		return sum

