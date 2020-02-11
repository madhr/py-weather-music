from mido import MidiFile

from appenders.appender_interface import AppenderInterface
from arp_pattern import ArpPattern
from converters import Converter
from melody_builder import MelodyBuilder
from sequences.humidity_sequence import HumiditySequence
from transposer import Transposer
from util.instruments import Instruments


class HumidityAppender(AppenderInterface):

	transposer = Transposer()
	converter = Converter()

	def append(self, melody_builder: MelodyBuilder, humidity_sequence: HumiditySequence) -> MidiFile:

		melody_builder.outfile = melody_builder.arpeggiator(
			program_value=Instruments.ElectricGuitar_muted,
			channel=4,
			pattern=ArpPattern.UP_AND_DOWN,
			track=humidity_sequence.get_track(),
			time_factor=240,
			scale=humidity_sequence.get_scale(),
			velocity=humidity_sequence.get_velocity()
		)
		return melody_builder.outfile