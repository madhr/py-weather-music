from mido import MidiFile

from appenders.appender_interface import AppenderInterface
from tracks.humidity_track import HumidityTrack
from util.arp_pattern import ArpPattern
from util.converters import Converter
from melody_builder import MelodyBuilder
from sequences.humidity_sequence import HumiditySequence
from util.transposer import Transposer


class HumidityAppender(AppenderInterface):

	transposer = Transposer()
	converter = Converter()

	def append(self, melody_builder: MelodyBuilder, humidity_sequence: HumiditySequence, humidity_track: HumidityTrack) -> MidiFile:

		melody_builder.outfile = melody_builder.arpeggiator(
			channel=humidity_track.get_channel(),
			pattern=ArpPattern.UP_AND_DOWN,
			track=humidity_sequence.get_track(),
			time_factor=240,
			scale=humidity_sequence.get_scale(),
			velocity=humidity_sequence.get_velocity()
		)
		return melody_builder.outfile