from mido import MidiFile

from appenders.appender_interface import AppenderInterface
from arp_pattern import ArpPattern
from converters import Converter
from melody_builder import MelodyBuilder
from sequences.temperature_sequence import TemperatureSequence
from util.chords import Chords
from util.instruments import Instruments


class TemperatureAppender(AppenderInterface):

	def append(self, melody_builder: MelodyBuilder, temperature_sequence: TemperatureSequence) -> MidiFile:

		melody_builder.outfile = melody_builder.arpeggiator(
			program_value=Instruments.BrightAcousticPiano,
			channel=1,
			pattern=ArpPattern.UP_AND_DOWN,
			track=temperature_sequence.get_track(),
			time_factor=60,
			scale=temperature_sequence.get_temperature_scale()
		)

		return melody_builder.outfile
