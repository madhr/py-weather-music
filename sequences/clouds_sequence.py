from mido import MidiTrack

from sequences.sequence import Sequence


class CloudsSequence(Sequence):

	def __init__(self, clouds: float, length: int, base_note: int, track: MidiTrack, music_scale=None):
		super().__init__(length, base_note, music_scale)
		self.__clouds = clouds
		self.__track = track

	def get_clouds(self):
		return self.__clouds

	def set_clouds(self, clouds: float):
		self.__clouds = clouds

	def get_track(self):
		return self.__track

