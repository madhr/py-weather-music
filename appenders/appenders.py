from abc import ABCMeta, abstractmethod

from mido import MidiFile

from melody_builder import MelodyBuilder
from sequences.sequences import Sequence, CloudsSequence, HumiditySequence, RainSequence, TemperatureSequence, WindSequence
from tracks.tracks import Track, CloudsTrack, HumidityTrack, RainTrack, TemperatureTrack, WindTrack
from util.arp_pattern import ArpPattern
from util.converters import Converter
from util.transposer import Transposer


class AppenderInterface:
	__metaclass__ = ABCMeta

	@abstractmethod
	def append(self, melody_builder: MelodyBuilder, sequence: Sequence, track: Track) -> MidiFile:
		raise NotImplementedError


class CloudsAppender(AppenderInterface):

	def append(self, melody_builder: MelodyBuilder, clouds_sequence: CloudsSequence, clouds_track: CloudsTrack) -> MidiFile:

		melody_builder.outfile = melody_builder.chord(
			channel=clouds_track.get_channel(),
			chord=clouds_sequence.get_chord(),
			track=clouds_sequence.get_track(),
			time_factor=clouds_sequence.get_length()
		)

		return melody_builder.outfile


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

class RainAppender(AppenderInterface):

	def append(self, melody_builder: MelodyBuilder, rain_sequence: RainSequence, rain_track: RainTrack) -> MidiFile:
		melody_builder.outfile = melody_builder.random(
			channel=rain_track.get_channel(),
			scale=rain_sequence.get_rain_scale(),
			track=rain_sequence.get_track(),
			time_factor=15
		)

		return melody_builder.outfile


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


class WindAppender(AppenderInterface):

	def append(self, melody_builder: MelodyBuilder, wind_sequence: WindSequence, wind_track: WindTrack) -> MidiFile:

		melody_builder.outfile = melody_builder.dynamic(
			channel=wind_track.get_channel(),
			note=wind_sequence.get_note(),
			track=wind_sequence.get_track(),
			velocity=wind_sequence.get_noise_level()
		)
		return melody_builder.outfile