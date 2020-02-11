from mido import MidiTrack


class Sequence:

	def __init__(self, length: int, base_note: int, track: MidiTrack):
		self.__length = length
		self.__base_note = base_note
		self.__track = track

	def get_length(self):
		return self.__length

	def get_base_note(self):
		return self.__base_note

	def get_track(self):
		return self.__track

	def set_base_note(self, base_note: int):
		self.__base_note = base_note

