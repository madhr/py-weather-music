from mido import MidiFile

from appenders.appender_interface import AppenderInterface
from melody_builder import MelodyBuilder
from sequences.clouds_sequence import CloudsSequence
from util.instruments import Instruments


class CloudsAppender(AppenderInterface):

	def append(self, melody_builder: MelodyBuilder, clouds_sequence: CloudsSequence) -> MidiFile:

		melody_builder.outfile = melody_builder.chord(
			program_value=Instruments.TremoloStrings,
			channel=3,
			chord=clouds_sequence.get_chord(),
			track=clouds_sequence.get_track(),
			time_factor=clouds_sequence.get_length()
		)

		return melody_builder.outfile