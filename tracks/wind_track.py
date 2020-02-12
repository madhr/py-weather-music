from mido import MidiTrack

from util.instruments import Instruments
from tracks.track import Track


class WindTrack(Track):

    def __init__(self, track: MidiTrack, channel: int, instrument: Instruments):
        super().__init__(track, channel, instrument)

    def get_track(self):
        return super().get_track()

    def get_channel(self):
        return super().get_channel()

    def get_instrument(self):
        return super().get_instrument()

