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
	converter = Converter()
	chords = Chords()
	transposer = Transposer()
	music_scales = MusicScales()

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
			self.append_temperature(melody_builder, temperature_track, base_note, entry.temperature)
			self.append_rain(melody_builder, rain_track, base_note, entry.weather.rain)
			self.append_clouds(melody_builder, clouds_track, base_note, entry.weather.clouds)
			self.append_humidity(melody_builder, humidity_track, base_note, entry.weather.humidity)
			self.append_wind(melody_builder, wind_track, base_note, entry.weather.wind_speed)

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
		print("file saved at " + file_dir + '/' + file_name + '.mid')
		return outfile

	def get_midi_track_time(self, midi_track: MidiTrack):
		sum = 0
		for message in midi_track:
			sum += message.time
		return sum

	def append_temperature(self, melody_builder: MelodyBuilder, temperature_track: MidiTrack, base_note: int, temperature: Temperature) -> MidiFile:

		amplitude = temperature.temp_max - temperature.temp_min
		notes_for_arp = self.converter.amplitude_to_arp_notes(amplitude, self.chords.minor_seventh(base_note))

		melody_builder.outfile = melody_builder.arpeggiator(
			program_value=Instruments.BrightAcousticPiano,
			channel=1,
			pattern=ArpPattern.UP_AND_DOWN,
			track=temperature_track,
			time_factor=60,
			scale=notes_for_arp
		)

		return melody_builder.outfile

	def append_rain(self, melody_builder: MelodyBuilder, rain_track: MidiTrack, base_note: int, rain: float) -> MidiFile:

		melodic_minor = self.music_scales.melodic_minor(base_note)
		scale = self.converter.rain_to_scale_size(rain, melodic_minor)
		scale = self.transposer.octave_up_list(scale)

		melody_builder.outfile = melody_builder.random(
			program_value=Instruments.Celesta,
			channel=2,
			scale=scale,
			track=rain_track,
			time_factor=15
		)

		return melody_builder.outfile

	def append_clouds(self, melody_builder: MelodyBuilder, clouds_track: MidiTrack, base_note: int, clouds: int) -> MidiFile:

		length = self.converter.clouds_to_chord_length(clouds)

		melody_builder.outfile = melody_builder.chord(
			program_value=Instruments.TremoloStrings,
			channel=3,
			chord=self.transposer.octave_down_list(self.chords.minor_seventh(base_note)),
			track=clouds_track,
			time_factor=length
		)

		return melody_builder.outfile

	def append_humidity(self, melody_builder: MelodyBuilder, humidity_track: MidiTrack, base_note: int, humidity: float) -> MidiFile:

		notes_for_arp = [self.transposer.two_octaves_down(base_note)]
		velocity = self.converter.humidity_to_volume(humidity)

		melody_builder.outfile = melody_builder.arpeggiator(
			program_value=Instruments.ElectricGuitar_muted,
			channel=4,
			pattern=ArpPattern.UP_AND_DOWN,
			track=humidity_track,
			time_factor=240,
			scale=notes_for_arp,
			velocity=velocity
		)
		return melody_builder.outfile

	def append_wind(self, melody_builder: MelodyBuilder, wind_track: MidiTrack, base_note: int, wind: float) -> MidiFile:

		noise_level = self.converter.wind_to_noise_level(wind)

		melody_builder.outfile = melody_builder.dynamic(
			program_value=Instruments.Seashore,
			channel=5,
			note=self.transposer.octave_down(base_note),
			track=wind_track,
			velocity=noise_level
		)
		return melody_builder.outfile