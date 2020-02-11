class MusicScale:

	def pentatonic(self, note) -> list:
		return [note, note + 3, note + 5, note + 7, note + 10]

	def melodic_minor(self, note) -> list:
		return [note, note + 2, note + 3, note + 5, note + 7, note + 8, note + 11]

	def minor(self, note) -> list:
		return [note, note + 2, note + 3, note + 5, note + 7, note + 8, note + 10]

	def major(self, note) -> list:
		return [note, note + 2, note + 4, note + 5, note + 7, note + 9, note + 11]
