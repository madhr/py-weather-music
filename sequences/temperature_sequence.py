from mido import MidiTrack

from sequences.sequence import Sequence


class TemperatureSequence(Sequence):

	def __init__(self, temperature: float, length: int, base_note: int, track: MidiTrack, music_scale=None):
		super().__init__(length, base_note, track, music_scale)
		self.__temperature = temperature

	def get_temperature(self):
		return self.__temperature

	def set_temperature(self, temperature: float):
		self.__temperature = temperature

