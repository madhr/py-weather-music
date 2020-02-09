import math
from arp_pattern import ArpPattern
from arpeggiator import Arpeggiator
from transposer import Transposer


class Converter:

	def list_of_notes_to_length(self, list_of_notes: list, length: int) -> list:
		if len(list_of_notes) > length:
			return list_of_notes[0:length]
		else:
			transposer = Transposer()
			new_list = list_of_notes + transposer.octave_up_list(list_of_notes)
			return self.list_of_notes_to_length(new_list, length)

	def amplitude_to_arp_notes(self, amplitude: int, list_of_notes: list) -> list:
		arpeggiator = Arpeggiator()
		normalized_amplitude = int(amplitude + 1) * 4
		amplitude_based_notes = self.list_of_notes_to_length(list_of_notes, normalized_amplitude)
		return arpeggiator.create(ArpPattern.UP_AND_DOWN, amplitude_based_notes)

	def temperature_to_base_note(self, feels_like: float) -> int:
		return int(feels_like / 4.2) - 6

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

	def humidity_to_volume(self, humidity: int):
		return int(humidity * 1.27)

	def wind_to_noise_level(self, wind: float) -> int:
		return int(wind*5) if wind < 25 else 127
