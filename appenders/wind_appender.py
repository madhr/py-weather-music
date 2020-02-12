from mido import MidiFile

from appenders.appender_interface import AppenderInterface
from melody_builder import MelodyBuilder
from sequences.wind_sequence import WindSequence
from tracks.wind_track import WindTrack


class WindAppender(AppenderInterface):

	def append(self, melody_builder: MelodyBuilder, wind_sequence: WindSequence, wind_track: WindTrack) -> MidiFile:

		melody_builder.outfile = melody_builder.dynamic(
			channel=wind_track.get_channel(),
			note=wind_sequence.get_note(),
			track=wind_sequence.get_track(),
			velocity=wind_sequence.get_noise_level()
		)
		return melody_builder.outfile