from mido import MidiTrack

from util.instruments import Instruments
from tracks.track import Track


class WindTrack(Track):

    track: MidiTrack
    name = 'wind'

    def __init__(self, channel: int, instrument: Instruments):
        self.track = MidiTrack()
        self.track.name = self.name
        super().__init__(self.track, channel, instrument)

    def get_track(self):
        return self.track

    def get_channel(self):
        return super().get_channel()

    def get_instrument(self):
        return super().get_instrument()

