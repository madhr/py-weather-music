from sequences.sequence import Sequence


class WindSequence(Sequence):

	def __init__(self, wind_speed: float):
		super().__init__()
		self.__wind_speed = wind_speed

	def get_wind_speed(self):
		return self.__wind_speed

	def set_wind_speed(self, wind_speed: float):
		self.__wind_speed = wind_speed

