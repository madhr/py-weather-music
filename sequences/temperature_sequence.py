from mido import MidiTrack

from converters import Converter
from sequences.sequence import Sequence
from util.chords import Chords
from weather_forecast import Temperature


class TemperatureSequence(Sequence):

	converter = Converter()
	chords = Chords()

	def __init__(self, temperature: Temperature, length: int, base_note: int, track: MidiTrack, music_scale=None):
		super().__init__(length, base_note, music_scale)
		self.__temperature = temperature
		self.__track = track
		self.__temperture_scale = self.converter.amplitude_to_arp_pattern((temperature.temp_max - temperature.temp_min), self.chords.minor_seventh(self.get_base_note()))

	def get_temperature(self):
		return self.__temperature

	def set_temperature(self, temperature: Temperature):
		self.__temperature = temperature

	def get_track(self):
		return self.__track

	def get_temperature_scale(self):
		return self.__temperture_scale