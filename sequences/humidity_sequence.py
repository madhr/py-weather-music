from mido import MidiTrack

from util.converters import Converter
from sequences.sequence import Sequence
from util.transposer import Transposer


class HumiditySequence(Sequence):

	transposer = Transposer()
	converter = Converter()

	def __init__(self, humidity: int, length: int, base_note: int, track: MidiTrack, music_scale=None):
		super().__init__(length, base_note, music_scale)
		self.__humidity = humidity
		self.__track = track
		self.__scale = [self.transposer.two_octaves_down(self.get_base_note())]
		self.__velocity = self.converter.humidity_to_velocity(self.get_humidity())

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