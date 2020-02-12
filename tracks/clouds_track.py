from mido import MidiTrack

from util.instruments import Instruments
from tracks.track import Track


class CloudsTrack(Track):

    track: MidiTrack
    name = 'clouds'

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

