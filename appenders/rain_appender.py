from mido import MidiFile

from appenders.appender_interface import AppenderInterface
from melody_builder import MelodyBuilder
from sequences.rain_sequence import RainSequence
from tracks.tracks import RainTrack


class RainAppender(AppenderInterface):

	def append(self, melody_builder: MelodyBuilder, rain_sequence: RainSequence, rain_track: RainTrack) -> MidiFile:

		melody_builder.outfile = melody_builder.random(
			channel=rain_track.get_channel(),
			scale=rain_sequence.get_rain_scale(),
			track=rain_sequence.get_track(),
			time_factor=15
		)

		return melody_builder.outfile