from util.arp_pattern import ArpPattern


class Arpeggiator:

    def create(self, pattern: ArpPattern, list_of_notes: list) -> list:
        if pattern == ArpPattern.UP:
            return self.__up(list_of_notes)
        elif pattern == ArpPattern.DOWN:
            return self.__down(list_of_notes)
        elif pattern == ArpPattern.UP_AND_DOWN:
            return self.__up_and_down(list_of_notes)
        else:
            raise Exception("Invalid ArpPattern enum")

    def __up(self, list_of_notes: list) -> list:
        return list_of_notes

    def __down(self, list_of_notes: list) -> list:
        return list(reversed(list_of_notes))

    def __up_and_down(self, list_of_notes: list) -> list:
        return self.__up(list_of_notes) + self.__down(list_of_notes[1:-1])

