import math
from arp_pattern import ArpPattern
from arpeggiator import Arpeggiator
from transposer import Transposer


class Converter:

	HUMIDITY_TO_VOLUME = 1.27
	WIND_TO_NOISE = 5
	CLOUDS_TO_CHORD_LENGTH = 12
	TEMPERATURE_TO_BASE_NOTE = 0.238
	TRANSPOSE_BASE_NOTE = -6
	MAX_NOISE_VALUE = 127
	EDGE_WIND_VALUE = 25
	AMPLITUDE_ADD = 1
	AMPLITUDE_MULTIPLY = 4

	def list_of_notes_to_length(self, list_of_notes: list, length: int) -> list:
		if len(list_of_notes) > length:
			return list_of_notes[0:length]
		else:
			transposer = Transposer()
			new_list = list_of_notes + transposer.octave_up_list(list_of_notes)
			return self.list_of_notes_to_length(new_list, length)

	def amplitude_to_arp_notes(self, amplitude: int, list_of_notes: list) -> list:
		arpeggiator = Arpeggiator()
		normalized_amplitude = int(amplitude + self.AMPLITUDE_ADD) * self.AMPLITUDE_MULTIPLY
		amplitude_based_notes = self.list_of_notes_to_length(list_of_notes, normalized_amplitude)
		return arpeggiator.create(ArpPattern.UP_AND_DOWN, amplitude_based_notes)

	def temperature_to_base_note(self, feels_like: float) -> int:
		transposer = Transposer()
		return transposer.transpose(int(feels_like * self.TEMPERATURE_TO_BASE_NOTE), self.TRANSPOSE_BASE_NOTE)

	def rain_to_scale_size(self, rain: float, scale: list) -> list:
		if len(scale) < 1:
			raise Exception("Missing scale")
		last_item = None
		if rain == 0:
			return None
		elif 0 < rain < 2:
			return [scale[0]]
		elif 2 <= rain < 30:
			last_item = int(math.sqrt(rain)) + 1
		elif 30 <= rain:
			last_item = 7
		return scale[0:last_item]

	def clouds_to_chord_length(self, clouds: int) -> int:
		return int(clouds * self.CLOUDS_TO_CHORD_LENGTH)

	def humidity_to_volume(self, humidity: int):
		return int(humidity * self.HUMIDITY_TO_VOLUME)

	def wind_to_noise_level(self, wind: float) -> int:
		return int(wind*self.WIND_TO_NOISE) if wind < self.EDGE_WIND_VALUE else self.MAX_NOISE_VALUE
