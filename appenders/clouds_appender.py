from mido import MidiFile

from appenders.appender_interface import AppenderInterface
from melody_builder import MelodyBuilder
from sequences.sequences import CloudsSequence
from tracks.tracks import CloudsTrack


class CloudsAppender(AppenderInterface):

	def append(self, melody_builder: MelodyBuilder, clouds_sequence: CloudsSequence, clouds_track: CloudsTrack) -> MidiFile:

		melody_builder.outfile = melody_builder.chord(
			channel=clouds_track.get_channel(),
			chord=clouds_sequence.get_chord(),
			track=clouds_sequence.get_track(),
			time_factor=clouds_sequence.get_length()
		)

		return melody_builder.outfile