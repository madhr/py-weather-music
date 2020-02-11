from pathlib import Path

from mido import MidiFile, MidiTrack

from appenders.wind_appender import WindAppender
from appenders.clouds_appender import CloudsAppender
from appenders.humidity_appender import HumidityAppender
from appenders.rain_appender import RainAppender
from appenders.temperature_appender import TemperatureAppender
from converters import Converter
from melody_builder import MelodyBuilder
from sequences.wind_sequence import WindSequence
from sequences.clouds_sequence import CloudsSequence
from sequences.humidity_sequence import HumiditySequence
from sequences.rain_sequence import RainSequence
from sequences.temperature_sequence import TemperatureSequence
from transposer import Transposer
from util.chords import Chords
from util.music_scale import MusicScale
from weather_api import WeatherApi


class WeatherToMusicConverter:

	TICKS_PER_BEAT = 400
	PHRASE_LENGTH = 1200
	converter = Converter()
	chords = Chords()
	transposer = Transposer()
	music_scales = MusicScale()

	def weather_to_music(self, api_key, city):
		api_handling = WeatherApi()

		weather_forecast = api_handling.get_weather_forecast_from_api(city, api_key)

		outfile = MidiFile()
		outfile.ticks_per_beat = self.TICKS_PER_BEAT

		temperature_track = MidiTrack()
		temperature_track.name = "temperature"
		rain_track = MidiTrack()
		rain_track.name = "rain"
		clouds_track = MidiTrack()
		clouds_track.name = "clouds"
		humidity_track = MidiTrack()
		humidity_track.name = "humidity"
		wind_track = MidiTrack()
		wind_track.name = "wind"

		melody_builder = MelodyBuilder(outfile, self.PHRASE_LENGTH)

		for entry in weather_forecast.weather_timestamps:
			base_note = self.converter.temperature_to_base_note(entry.temperature.feels_like)

			music_scale = self.music_scales.melodic_minor(base_note)

			temperature_sequence = TemperatureSequence(entry.temperature, self.PHRASE_LENGTH, base_note, temperature_track)
			temperature_appender = TemperatureAppender()
			temperature_appender.append(melody_builder, temperature_sequence)

			rain_sequence = RainSequence(entry.weather.rain, self.PHRASE_LENGTH, base_note, rain_track, music_scale)
			rain_appender = RainAppender()
			rain_appender.append(melody_builder, rain_sequence)

			clouds_sequence = CloudsSequence(entry.weather.clouds, self.PHRASE_LENGTH, base_note, clouds_track)
			clouds_appender = CloudsAppender()
			clouds_appender.append(melody_builder, clouds_sequence)

			humidity_sequence = HumiditySequence(entry.weather.humidity, self.PHRASE_LENGTH, base_note, humidity_track)
			humidity_appender = HumidityAppender()
			humidity_appender.append(melody_builder, humidity_sequence)

			wind_sequence = WindSequence(entry.weather.wind_speed, self.PHRASE_LENGTH, base_note, wind_track)
			wind_appender = WindAppender()
			wind_appender.append(melody_builder, wind_sequence)

		outfile.tracks.append(temperature_track)
		outfile.tracks.append(rain_track)
		outfile.tracks.append(clouds_track)
		outfile.tracks.append(humidity_track)
		outfile.tracks.append(wind_track)

		file_dir = 'midi_out'
		file_name = 'song-for-' + city + str(weather_forecast.sunrise)
		self.save_file(outfile, file_dir, file_name)

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

