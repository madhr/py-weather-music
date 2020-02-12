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


class HumidityTrack(Track):
    track: MidiTrack
    name = 'humidity'

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


class RainTrack(Track):

    track: MidiTrack
    name = 'rain'

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


class TemperatureTrack(Track):

    track: MidiTrack
    name = 'temperature'

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

