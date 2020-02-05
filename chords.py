class Chords:

	def minor_triad(self, note):
		return [note, note + 3, note + 7]

	def major_triad(self, note):
		return [note, note + 4, note + 7]

	def minor_seventh(self, note):
		chord = self.minor_triad(note)
		chord.append(note + 11)
		return chord

	def major_seventh(self, note):
		chord = self.major_triad(note)
		chord.append(note + 11)
		return chord
