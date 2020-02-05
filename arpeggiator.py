from arp_pattern import ArpPattern


class Arpeggiator:

    def create(self, pattern, list_of_notes):
        if pattern == ArpPattern.UP:
            return self.__up(list_of_notes)
        elif pattern == ArpPattern.DOWN:
            return self.__down(list_of_notes)
        elif pattern == ArpPattern.UP_AND_DOWN:
            return self.__up_and_down(list_of_notes)
        else:
            raise Exception("Invalid ArpPattern enum")

    def __up(self, list_of_notes):
        return list_of_notes

    def __down(self, list_of_notes):
        return list(reversed(list_of_notes))

    def __up_and_down(self, list_of_notes):
        return self.up(list_of_notes) + self.down(list_of_notes[1:-1])

