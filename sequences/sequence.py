from mido import MidiTrack

from util.music_scale import MusicScale


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

