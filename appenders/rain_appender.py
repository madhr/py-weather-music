from mido import MidiFile

from appenders.appender_interface import AppenderInterface
from converters import Converter
from melody_builder import MelodyBuilder
from sequences.rain_sequence import RainSequence
from transposer import Transposer
from util.instruments import Instruments


class RainAppender(AppenderInterface):

	converter = Converter()
	transposer = Transposer()

	def append(self, melody_builder: MelodyBuilder, rain_sequence: RainSequence) -> MidiFile:

		rain_scale = self.converter.rain_to_scale_size(rain_sequence.get_rain(), rain_sequence.get_music_scale())
		rain_scale = self.transposer.octave_up_list(rain_scale)

		melody_builder.outfile = melody_builder.random(
			program_value=Instruments.Celesta,
			channel=2,
			scale=rain_scale,
			track=rain_sequence.get_track(),
			time_factor=15
		)

		return melody_builder.outfile