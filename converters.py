import math
from arp_pattern import ArpPattern
from arpeggiator import Arpeggiator


class Converter:

	def amplitude_to_arp_notes(self, amplitude: int, list_of_notes: list) -> list:
		arpeggiator = Arpeggiator()
		if 0 <= amplitude < 3:
			return arpeggiator.create(ArpPattern.UP_AND_DOWN, list_of_notes)
		elif 3 <= amplitude < 6:
			return arpeggiator.create(ArpPattern.UP_2_OCTAVES, list_of_notes)
		elif 6 <= amplitude < 15:
			return arpeggiator.create(ArpPattern.DOWN_2_OCTAVES, list_of_notes)
		elif 15 <= amplitude:
			return arpeggiator.create(ArpPattern.UP_AND_DOWN_2_OCTAVES, list_of_notes)

	def temperature_to_base_note(self, feels_like: float) -> int:
		return int(feels_like / 4.2)

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
		return int(clouds * 12)
