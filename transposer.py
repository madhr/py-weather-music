class Transposer:

    def transpose(self, note: int, value: int):
        return note + value

    def transpose_list(self, notes: list, value: int):
        transposed = [note+value for note in notes]
        return transposed

    def octave_up(self, note):
        return self.transpose(note, 12)

    def octave_up_list(self, notes: list):
        return self.transpose_list(notes, 12)

    def octave_down(self, note):
        return self.transpose(note, -12)

    def octave_down_list(self, notes: list):
        return self.transpose_list(notes, -12)

