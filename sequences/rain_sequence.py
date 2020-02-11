from sequences.sequence import Sequence


class RainSequence(Sequence):

	def __init__(self, rain: float):
		super().__init__()
		self.__rain = rain

	def get_rain(self):
		return self.__rain

	def set_rain(self, rain: float):
		self.__rain = rain

