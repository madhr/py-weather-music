from mido import MidiTrack

from util.instruments import Instruments


class Track:

    def __init__(self, track: MidiTrack, channel: int, instrument: Instruments):
        self.__track = track
        self.__channel = channel
        self.__instrument = instrument

    def get_track(self):
        return self.__track

    def get_channel(self):
        return self.__channel

    def get_instrument(self):
        return self.__instrument

