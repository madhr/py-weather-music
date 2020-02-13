from music_rules.arp_pattern import ArpPattern
from music_rules.transposer import Transposer


class Arpeggiator:

    transposer = Transposer()

    def create(self, pattern: ArpPattern, list_of_notes: list) -> list:
        if pattern == ArpPattern.UP:
            return self.__up(list_of_notes)
        elif pattern == ArpPattern.DOWN:
            return self.__down(list_of_notes)
        elif pattern == ArpPattern.UP_AND_DOWN:
            return self.__up_and_down(list_of_notes)
        elif pattern == ArpPattern.UP_2_OCTAVES:
            return self.__up_2_octaves(list_of_notes)
        elif pattern == ArpPattern.DOWN_2_OCTAVES:
            return self.__down_2_octaves(list_of_notes)
        elif pattern == ArpPattern.UP_AND_DOWN_2_OCTAVES:
            return self.__up_and_down_2_octaves(list_of_notes)
        else:
            raise Exception("Invalid ArpPattern enum")

    def __up(self, list_of_notes: list) -> list:
        return list_of_notes

    def __down(self, list_of_notes: list) -> list:
        return list(reversed(list_of_notes))

    def __up_and_down(self, list_of_notes: list) -> list:
        return self.__up(list_of_notes) + self.__down(list_of_notes[1:-1])

    def __up_2_octaves(self, list_of_notes: list) -> list:
        return self.__up(self.__get_list_of_notes_2_octaves(list_of_notes))

    def __down_2_octaves(self, list_of_notes: list) -> list:
        return self.__down(self.__get_list_of_notes_2_octaves(list_of_notes))

    def __up_and_down_2_octaves(self, list_of_notes: list) -> list:
        return self.__up_and_down(self.__get_list_of_notes_2_octaves(list_of_notes))

    def __get_list_of_notes_2_octaves(self, list_of_notes: list) -> list:
        return list_of_notes + self.transposer.octave_up_list(list_of_notes)