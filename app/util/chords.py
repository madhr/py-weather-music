class Chords:

	def minor_triad(self, note: int) -> list:
		return [note, note + 3, note + 7]

	def major_triad(self, note: int) -> list:
		return [note, note + 4, note + 7]

	def minor_seventh(self, note: int) -> list:
		chord = self.minor_triad(note)
		chord.append(note + 10)
		return chord

	def major_seventh(self, note: int) -> list:
		chord = self.major_triad(note)
		chord.append(note + 10)
		return chord
