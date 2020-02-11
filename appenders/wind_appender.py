from mido import MidiFile

from appenders.appender_interface import AppenderInterface
from melody_builder import MelodyBuilder
from sequences.wind_sequence import WindSequence
from util.instruments import Instruments


class WindAppender(AppenderInterface):

	def append(self, melody_builder: MelodyBuilder, wind_sequence: WindSequence) -> MidiFile:

		melody_builder.outfile = melody_builder.dynamic(
			program_value=Instruments.Seashore,
			channel=5,
			note=wind_sequence.get_note(),
			track=wind_sequence.get_track(),
			velocity=wind_sequence.get_noise_level()
		)
		return melody_builder.outfile