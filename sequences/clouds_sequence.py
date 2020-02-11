from mido import MidiTrack

from util.converters import Converter
from sequences.sequence import Sequence
from util.transposer import Transposer
from util.chords import Chords


class CloudsSequence(Sequence):

	chords = Chords()
	converter = Converter()
	transposer = Transposer()

	def __init__(self, clouds: int, length: int, base_note: int, track: MidiTrack, music_scale=None):
		super().__init__(length, base_note, music_scale)
		self.__clouds = clouds
		self.__track = track
		self.__length = self.converter.clouds_to_chord_length(self.get_clouds())
		self.__chord = self.transposer.octave_down_list(self.chords.minor_seventh(self.get_base_note()))

	def get_clouds(self):
		return self.__clouds

	def set_clouds(self, clouds: float):
		self.__clouds = clouds

	def get_track(self):
		return self.__track

	def get_length(self):
		return self.__length

	def get_chord(self):
		return self.__chord

