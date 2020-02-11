from mido import MidiTrack

from sequences.sequence import Sequence
from util.music_scale import MusicScale


class RainSequence(Sequence):

	def __init__(self, rain: float, length: int, base_note: int, track: MidiTrack, music_scale: list):
		super().__init__(length, base_note, music_scale)
		self.__rain = rain
		self.__track = track

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

