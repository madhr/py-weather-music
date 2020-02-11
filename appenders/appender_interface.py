from abc import ABCMeta, abstractmethod

from mido import MidiFile

from melody_builder import MelodyBuilder
from sequences.sequence import Sequence


class AppenderInterface:
	__metaclass__ = ABCMeta

	@abstractmethod
	def append(self, melody_builder: MelodyBuilder, sequence: Sequence) -> MidiFile:
		raise NotImplementedError

