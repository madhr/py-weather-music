from mido import MidiTrack

from sequences.sequence import Sequence


class WindSequence(Sequence):

	def __init__(self, wind_speed: float, length: int, base_note: int, track: MidiTrack, music_scale=None):
		super().__init__(length, base_note, track, music_scale)
		self.__wind_speed = wind_speed

	def get_wind_speed(self):
		return self.__wind_speed

	def set_wind_speed(self, wind_speed: float):
		self.__wind_speed = wind_speed

