from sequences.sequence import Sequence


class TemperatureSequence(Sequence):

	def __init__(self, temperature: float):
		super().__init__()
		self.__temperature = temperature

	def get_temperature(self):
		return self.__temperature

	def set_temperature(self, temperature: float):
		self.__temperature = temperature

