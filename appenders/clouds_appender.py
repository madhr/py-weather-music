from mido import MidiFile

from appenders.appender_interface import AppenderInterface
from converters import Converter
from melody_builder import MelodyBuilder
from sequences.clouds_sequence import CloudsSequence
from transposer import Transposer
from util.chords import Chords
from util.instruments import Instruments


class CloudsAppender(AppenderInterface):

	chords = Chords()
	converter = Converter()
	transposer = Transposer()

	def append(self, melody_builder: MelodyBuilder, clouds_sequence: CloudsSequence) -> MidiFile:

		length = self.converter.clouds_to_chord_length(clouds_sequence.get_clouds())

		melody_builder.outfile = melody_builder.chord(
			program_value=Instruments.TremoloStrings,
			channel=3,
			chord=self.transposer.octave_down_list(self.chords.minor_seventh(clouds_sequence.get_base_note())),
			track=clouds_sequence.get_track(),
			time_factor=length
		)

		return melody_builder.outfile