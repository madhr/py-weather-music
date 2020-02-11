from sequences.sequence import Sequence


class CloudsSequence(Sequence):

	def __init__(self, clouds: float):
		super().__init__()
		self.__clouds = clouds

	def get_clouds(self):
		return self.__clouds

	def set_clouds(self, clouds: float):
		self.__clouds = clouds

