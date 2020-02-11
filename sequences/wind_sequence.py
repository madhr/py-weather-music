from mido import MidiTrack

from converters import Converter
from sequences.sequence import Sequence
from transposer import Transposer


class WindSequence(Sequence):

	transposer = Transposer()
	converter = Converter()

	def __init__(self, wind_speed: float, length: int, base_note: int, track: MidiTrack, music_scale=None):
		super().__init__(length, base_note, music_scale)
		self.__wind_speed = wind_speed
		self.__track = track
		self.__noise_level = self.converter.wind_to_noise_level(self.get_wind_speed())
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
