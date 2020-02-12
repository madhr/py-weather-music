from abc import ABCMeta, abstractmethod

from mido import MidiFile

from app.tracks.tracks import *
from app.sequences.sequences import *
from app.util.melody_builder import MelodyBuilder


class AppenderInterface:
	__metaclass__ = ABCMeta

	@abstractmethod
	def append(self, melody_builder: MelodyBuilder, sequence: Sequence, track: Track) -> MidiFile:
		raise NotImplementedError


class CloudsAppender(AppenderInterface):

	def append(self, melody_builder: MelodyBuilder, sequence: CloudsSequence, track: CloudsTrack) -> MidiFile:

		melody_builder.outfile = melody_builder.chord(
			channel=track.get_channel(),
			chord=sequence.get_chord(),
			track=sequence.get_track(),
			time_factor=sequence.get_length()
		)
		return melody_builder.outfile


class HumidityAppender(AppenderInterface):

	def append(self, melody_builder: MelodyBuilder, sequence: HumiditySequence, track: HumidityTrack) -> MidiFile:

		melody_builder.outfile = melody_builder.arpeggiator(
			channel=track.get_channel(),
			pattern=sequence.get_pattern(),
			track=sequence.get_track(),
			time_factor=sequence.get_time_factor(),
			scale=sequence.get_scale(),
			velocity=sequence.get_velocity()
		)
		return melody_builder.outfile


class RainAppender(AppenderInterface):

	def append(self, melody_builder: MelodyBuilder, sequence: RainSequence, track: RainTrack) -> MidiFile:

		melody_builder.outfile = melody_builder.random(
			channel=track.get_channel(),
			scale=sequence.get_rain_scale(),
			track=sequence.get_track(),
			time_factor=sequence.get_time_factor()
		)
		return melody_builder.outfile


class TemperatureAppender(AppenderInterface):

	def append(self, melody_builder: MelodyBuilder, sequence: TemperatureSequence, track: TemperatureTrack) -> MidiFile:

		melody_builder.outfile = melody_builder.arpeggiator(
			channel=track.get_channel(),
			pattern=sequence.get_pattern(),
			track=sequence.get_track(),
			time_factor=sequence.get_time_factor(),
			scale=sequence.get_temperature_scale()
		)
		return melody_builder.outfile


class WindAppender(AppenderInterface):

	def append(self, melody_builder: MelodyBuilder, sequence: WindSequence, track: WindTrack) -> MidiFile:

		melody_builder.outfile = melody_builder.dynamic(
			channel=track.get_channel(),
			note=sequence.get_note(),
			track=sequence.get_track(),
			velocity=sequence.get_noise_level()
		)
		return melody_builder.outfile

