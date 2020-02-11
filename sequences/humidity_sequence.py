from sequences.sequence import Sequence


class HumiditySequence(Sequence):

	def __init__(self, humidity: float):
		super().__init__()
		self.__humidity = humidity

	def get_humidity(self):
		return self.__humidity

	def set_humidity(self, humidity: float):
		self.__humidity = humidity

