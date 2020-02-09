from pathlib import Path

from mido import MidiFile, MidiTrack

from arp_pattern import ArpPattern
from converters import Converter
from melody_builder import MelodyBuilder
from transposer import Transposer
from util.chords import Chords
from util.instruments import Instruments
from util.music_scales import MusicScales
from weather_api import WeatherApi
from weather_forecast import Temperature


class WeatherToMusicConverter:

	TICKS_PER_BEAT = 400
	PHRASE_LENGTH = 1200

	def weather_to_music(self, api_key, city):

		api_handling = WeatherApi()

		json_weather_forecast = api_handling.get_json_weather_forecast_from_api(city, api_key)

		if json_weather_forecast is None:
			raise Exception("Failed to pull weather forecast")

		weather_forecast = api_handling.parse_weather_forecast(json_weather_forecast)

		outfile = MidiFile()
		outfile.ticks_per_beat = self.TICKS_PER_BEAT

		conv = Converter()

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

		for entry in weather_forecast.weather_timestamps:

			base_note = conv.temperature_to_base_note(entry.temperature.feels_like)
			self.append_temperature(outfile, temperature_track, base_note, entry.temperature)
			self.append_rain(outfile, rain_track, base_note, entry.weather.rain)
			self.append_clouds(outfile, clouds_track, base_note, entry.weather.clouds)
			self.append_humidity(outfile, humidity_track, base_note, entry.weather.humidity)
			self.append_wind(outfile, wind_track, base_note, entry.weather.wind_speed)

		outfile.tracks.append(temperature_track)
		outfile.tracks.append(rain_track)
		outfile.tracks.append(clouds_track)
		outfile.tracks.append(humidity_track)
		outfile.tracks.append(wind_track)

		file_dir = 'midi_out'
		file_name = 'song-for-' + city
		self.save_file(outfile, file_dir, file_name)

	def save_file(self, outfile: MidiFile, file_dir: str, file_name: str) -> MidiFile:
		Path(file_dir).mkdir(exist_ok=True)
		outfile.save(file_dir + '/' + file_name + '.mid')
		print("file saved at " + file_dir + '/' + file_name)
		return outfile

	def get_midi_track_time(self, midi_track: MidiTrack):
		sum = 0
		for message in midi_track:
			sum += message.time
		return sum

	def append_temperature(self, outfile: MidiFile, temperature_track: MidiTrack, base_note: int, temperature: Temperature) -> MidiFile:
		conv = Converter()
		chords = Chords()
		melody_builder = MelodyBuilder(outfile, self.PHRASE_LENGTH)
		amplitude = temperature.temp_max - temperature.temp_min
		notes_for_arp = conv.amplitude_to_arp_notes(amplitude, chords.minor_seventh(base_note))

		outfile = melody_builder.arpeggiator(
			program_value=Instruments.Piccolo,
			channel=1,
			pattern=ArpPattern.UP_AND_DOWN,
			track=temperature_track,
			time_factor=60,
			scale=notes_for_arp
		)

		return outfile

	def append_rain(self, outfile: MidiFile, rain_track: MidiTrack, base_note: int, rain: float) -> MidiFile:
		conv = Converter()
		transposer = Transposer()
		melody_builder = MelodyBuilder(outfile, self.PHRASE_LENGTH)
		music_scales = MusicScales()
		melodic_minor = music_scales.melodic_minor(base_note)
		scale = conv.rain_to_scale_size(rain, melodic_minor)
		scale = transposer.octave_down_list(scale)
		outfile = melody_builder.random(
			program_value=Instruments.Celesta,
			channel=2,
			scale=scale,
			track=rain_track,
			time_factor=15
		)

		return outfile

	def append_clouds(self, outfile: MidiFile, clouds_track: MidiTrack, base_note: int, clouds: int) -> MidiFile:
		conv = Converter()
		melody_builder = MelodyBuilder(outfile, self.PHRASE_LENGTH)
		chords = Chords()

		length = conv.clouds_to_chord_length(clouds)
		outfile = melody_builder.chord(
			program_value=Instruments.Contrabass,
			channel=3,
			chord=chords.minor_seventh(base_note),
			track=clouds_track,
			time_factor=length
		)

		return outfile

	def append_humidity(self, outfile: MidiFile, humidity_track: MidiTrack, base_note: int, humidity: float) -> MidiFile:

		return outfile

	def append_wind(self, outfile: MidiFile, wind_track: MidiTrack, base_note: int, wind: float) -> MidiFile:

		return outfile