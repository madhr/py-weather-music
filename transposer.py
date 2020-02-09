class Transposer:

    def transpose(self, note: int, value: int) -> int:
        if note is None:
            return None
        return note + value

    def transpose_list(self, notes: list, value: int) -> list:
        if notes is None:
            return None
        transposed = [note+value for note in notes]
        return transposed

    def octave_up(self, note: int) -> int:
        if note is None:
            return None
        return self.transpose(note, 12)

    def octave_up_list(self, notes: list) -> list:
        if notes is None:
            return None
        return self.transpose_list(notes, 12)

    def octave_down(self, note: int) -> int:
        if note is None:
            return None
        return self.transpose(note, -12)

    def octave_down_list(self, notes: list) -> list:
        if notes is None:
            return None
        return self.transpose_list(notes, -12)

