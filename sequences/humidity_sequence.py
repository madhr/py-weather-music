from mido import MidiTrack

from sequences.sequence import Sequence


class HumiditySequence(Sequence):

	def __init__(self, humidity: float, length: int, base_note: int, track: MidiTrack, music_scale=None):
		super().__init__(length, base_note, music_scale)
		self.__humidity = humidity
		self.__track = track

	def get_humidity(self):
		return self.__humidity

	def set_humidity(self, humidity: float):
		self.__humidity = humidity

	def get_track(self):
		return self.__track

