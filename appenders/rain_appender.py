from mido import MidiFile

from appenders.appender_interface import AppenderInterface
from melody_builder import MelodyBuilder
from sequences.rain_sequence import RainSequence
from util.instruments import Instruments


class RainAppender(AppenderInterface):

	def append(self, melody_builder: MelodyBuilder, rain_sequence: RainSequence) -> MidiFile:

		melody_builder.outfile = melody_builder.random(
			program_value=Instruments.Celesta,
			channel=2,
			scale=rain_sequence.get_rain_scale(),
			track=rain_sequence.get_track(),
			time_factor=15
		)

		return melody_builder.outfile