from unittest import TestCase

from mido import MidiFile, MidiTrack

from app.util.melody_builder import MelodyBuilder


class TestMelodyBuilder(TestCase):



    def test_random(self):
        melody_builder = MelodyBuilder(outfile=MidiFile(), time_limit=120)
        track = MidiTrack()
        channel = 1
        scale = [5, 7]
        random = melody_builder.random(channel, scale, track)
        self.fail()


    def test_arpeggiator(self):
        self.fail()

    def test_chord(self):
        self.fail()

    def test_dynamic(self):
        self.fail()

    def test_set_instrument(self):
        self.fail()
