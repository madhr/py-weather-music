from mido import MidiTrack

from sequences.sequence import Sequence


class RainSequence(Sequence):

	def __init__(self, rain: float, length: int, base_note: int, track: MidiTrack, music_scale=None):
		super().__init__(length, base_note, track, music_scale)
		self.__rain = rain

	def get_rain(self):
		return self.__rain

	def set_rain(self, rain: float):
		self.__rain = rain

