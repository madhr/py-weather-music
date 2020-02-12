from abc import ABCMeta, abstractmethod

from mido import MidiFile

from melody_builder import MelodyBuilder
from sequences.sequence import Sequence
from tracks.tracks import Track


class AppenderInterface:
	__metaclass__ = ABCMeta

	@abstractmethod
	def append(self, melody_builder: MelodyBuilder, sequence: Sequence, track: Track) -> MidiFile:
		raise NotImplementedError

