from mido import MidiTrack

from util.arp_pattern import ArpPattern
from util.chords import Chords
from util.converters import Converter
from util.music_scale import MusicScale
from util.transposer import Transposer
from weather_api.weather_forecast import Temperature


class Sequence:

	def __init__(self, length: int, base_note: int, music_scale=None):
		self.__length = length
		self.__base_note = base_note
		self.__music_scale = music_scale

	def get_length(self):
		return self.__length

	def get_base_note(self):
		return self.__base_note

	def get_music_scale(self):
		return self.__music_scale

	def set_base_note(self, base_note: int):
		self.__base_note = base_note

	def set_music_scale(self, music_scale: MusicScale):
		self.__music_scale = music_scale


class CloudsSequence(Sequence):

	chords = Chords()
	converter = Converter()
	transposer = Transposer()

	def __init__(self, clouds: int, length: int, base_note: int, track: MidiTrack, music_scale=None):
		super().__init__(length, base_note, music_scale)
		self.__clouds = clouds
		self.__track = track
		self.__length = self.converter.clouds_to_chord_length(self.get_clouds())
		self.__chord = self.transposer.octave_down_list(self.chords.minor_seventh(self.get_base_note()))

	def get_clouds(self):
		return self.__clouds

	def set_clouds(self, clouds: float):
		self.__clouds = clouds

	def get_track(self):
		return self.__track

	def get_length(self):
		return self.__length

	def get_chord(self):
		return self.__chord


class HumiditySequence(Sequence):

	transposer = Transposer()
	converter = Converter()

	def __init__(self, humidity: int, length: int, base_note: int, track: MidiTrack, music_scale=None, time_factor=240, pattern=ArpPattern.UP_AND_DOWN):
		super().__init__(length, base_note, music_scale)
		self.__humidity = humidity
		self.__track = track
		self.__scale = [self.transposer.two_octaves_down(self.get_base_note())]
		self.__velocity = self.converter.humidity_to_velocity(self.get_humidity())
		self.__time_factor = time_factor
		self.__pattern = pattern

	def get_humidity(self):
		return self.__humidity

	def set_humidity(self, humidity: int):
		self.__humidity = humidity

	def get_track(self):
		return self.__track

	def get_scale(self):
		return self.__scale

	def get_velocity(self):
		return self.__velocity

	def get_time_factor(self):
		return self.__time_factor

	def get_pattern(self):
		return self.__pattern


class RainSequence(Sequence):

	converter = Converter()
	transposer = Transposer()

	def __init__(self, rain: float, length: int, base_note: int, track: MidiTrack, music_scale: list, time_factor=15):
		super().__init__(length, base_note, music_scale)
		self.__rain = rain
		self.__track = track
		self.__rain_scale = self.transposer.octave_up_list(self.converter.rain_to_scale_size(self.get_rain(), self.get_music_scale()))
		self.__time_factor = time_factor

	def get_rain(self):
		return self.__rain

	def set_rain(self, rain: float):
		self.__rain = rain

	def get_music_scale(self):
		return super().get_music_scale()

	def set_music_scale(self, music_scale: MusicScale):
		super().set_music_scale(music_scale)

	def get_track(self):
		return self.__track

	def get_rain_scale(self):
		return self.__rain_scale

	def get_time_factor(self):
		return self.__time_factor


class TemperatureSequence(Sequence):

	converter = Converter()
	chords = Chords()

	def __init__(self, temperature: Temperature, length: int, base_note: int, track: MidiTrack, music_scale=None, time_factor=60, pattern=ArpPattern.UP_AND_DOWN):
		super().__init__(length, base_note, music_scale)
		self.__temperature = temperature
		self.__track = track
		self.__temperture_scale = self.converter.amplitude_to_arp_pattern((temperature.temp_max - temperature.temp_min), self.chords.minor_seventh(self.get_base_note()))
		self.__time_factor = time_factor
		self.__pattern = pattern

	def get_temperature(self):
		return self.__temperature

	def set_temperature(self, temperature: Temperature):
		self.__temperature = temperature

	def get_track(self):
		return self.__track

	def get_temperature_scale(self):
		return self.__temperture_scale

	def get_time_factor(self):
		return self.__time_factor

	def get_pattern(self):
		return self.__pattern


class WindSequence(Sequence):

	transposer = Transposer()
	converter = Converter()

	def __init__(self, wind_speed: float, length: int, base_note: int, track: MidiTrack, music_scale=None):
		super().__init__(length, base_note, music_scale)
		self.__wind_speed = wind_speed
		self.__track = track
		self.__noise_level = self.converter.wind_to_velocity(self.get_wind_speed())
		self.__note = self.transposer.octave_down(self.get_base_note())

	def get_wind_speed(self):
		return self.__wind_speed

	def set_wind_speed(self, wind_speed: float):
		self.__wind_speed = wind_speed

	def get_track(self):
		return self.__track

	def get_note(self):
		return self.__note

	def get_noise_level(self):
		return self.__noise_level
