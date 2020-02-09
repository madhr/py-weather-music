from enum import Enum


class TemperatureEnum(Enum):
	TWO = range(0, 1),
	THREE = range(1,3),
	FOUR = range(3,6),
	SIX = range(6,15),
	EIGHT = range(15,30),
	TWELVE = range(30, )