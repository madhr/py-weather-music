from mido import MidiFile

from appenders.appender_interface import AppenderInterface
from tracks.temperature_track import TemperatureTrack
from util.arp_pattern import ArpPattern
from melody_builder import MelodyBuilder
from sequences.temperature_sequence import TemperatureSequence


class TemperatureAppender(AppenderInterface):

	def append(self, melody_builder: MelodyBuilder, temperature_sequence: TemperatureSequence, temperature_track: TemperatureTrack) -> MidiFile:

		melody_builder.outfile = melody_builder.arpeggiator(
			channel=temperature_track.get_channel(),
			pattern=ArpPattern.UP_AND_DOWN,
			track=temperature_sequence.get_track(),
			time_factor=60,
			scale=temperature_sequence.get_temperature_scale()
		)

		return melody_builder.outfile
