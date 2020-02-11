from mido import MidiTrack

from util.converters import Converter
from sequences.sequence import Sequence
from util.transposer import Transposer
from util.music_scale import MusicScale


class RainSequence(Sequence):

	converter = Converter()
	transposer = Transposer()

	def __init__(self, rain: float, length: int, base_note: int, track: MidiTrack, music_scale: list):
		super().__init__(length, base_note, music_scale)
		self.__rain = rain
		self.__track = track
		self.__rain_scale = self.transposer.octave_up_list(self.converter.rain_to_scale_size(self.get_rain(), self.get_music_scale()))

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

	def get_rain_scale(self):
		return self.__rain_scale