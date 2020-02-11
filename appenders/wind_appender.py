from mido import MidiFile

from appenders.appender_interface import AppenderInterface
from converters import Converter
from melody_builder import MelodyBuilder
from sequences.wind_sequence import WindSequence
from transposer import Transposer
from util.instruments import Instruments


class WindAppender(AppenderInterface):

	transposer = Transposer()
	converter = Converter()

	def append(self, melody_builder: MelodyBuilder, wind_sequence: WindSequence) -> MidiFile:

		noise_level = self.converter.wind_to_noise_level(wind_sequence.get_wind_speed())

		melody_builder.outfile = melody_builder.dynamic(
			program_value=Instruments.Seashore,
			channel=5,
			note=self.transposer.octave_down(wind_sequence.get_base_note()),
			track=wind_sequence.get_track(),
			velocity=noise_level
		)
		return melody_builder.outfile