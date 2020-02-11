from mido import MidiFile

from appenders.appender_interface import AppenderInterface
from arp_pattern import ArpPattern
from converters import Converter
from melody_builder import MelodyBuilder
from sequences.temperature_sequence import TemperatureSequence
from util.chords import Chords
from util.instruments import Instruments


class TemperatureAppender(AppenderInterface):

	converter = Converter()
	chords = Chords()

	def append(self, melody_builder: MelodyBuilder, temperature_sequence: TemperatureSequence) -> MidiFile:

		temperature = temperature_sequence.get_temperature()

		amplitude = temperature.temp_max - temperature.temp_min
		notes_for_arp = self.converter.amplitude_to_arp_notes(amplitude, self.chords.minor_seventh(temperature_sequence.get_base_note()))

		melody_builder.outfile = melody_builder.arpeggiator(
			program_value=Instruments.BrightAcousticPiano,
			channel=1,
			pattern=ArpPattern.UP_AND_DOWN,
			track=temperature_sequence.get_track(),
			time_factor=60,
			scale=notes_for_arp
		)

		return melody_builder.outfile
