from unittest import TestCase

from mido import MidiFile, MidiTrack

from build_midi.melody_builder import MelodyBuilder
from music_rules.arp_pattern import ArpPattern
from music_rules.chords import Chords
from music_rules.instruments import Instruments


class TestMelodyBuilder(TestCase):



    def test_random(self):
        time_limit = 120
        track = MidiTrack()
        melody_builder = MelodyBuilder(outfile=MidiFile(), time_limit=time_limit)
        melody_builder.random(channel=1, scale=[5, 7], track=track)
        sum = 0
        for mes in track:
            sum += mes.time
        self.assertEqual(sum, time_limit * 2)


    def test_arpeggiator(self):
        time_limit = 120
        track = MidiTrack()
        melody_builder = MelodyBuilder(outfile=MidiFile(), time_limit=time_limit)
        melody_builder.arpeggiator(channel=1, pattern=ArpPattern.UP, track=track, time_factor=time_limit, scale=[5, 7])
        sum = 0
        for mes in track:
            sum += mes.time
        self.assertEqual(sum, time_limit * 2)

    def test_chord(self):
        time_limit = 120
        track = MidiTrack()
        melody_builder = MelodyBuilder(outfile=MidiFile(), time_limit=time_limit)
        chords = Chords()
        melody_builder.chord(channel=1, chord=chords.major_seventh(note=60), track=track, time_factor=time_limit)
        sum = 0
        for mes in track:
            sum += mes.time
        self.assertEqual(sum, time_limit * 2)

    def test_dynamic(self):
        time_limit = 120
        track = MidiTrack()
        melody_builder = MelodyBuilder(outfile=MidiFile(), time_limit=time_limit)
        melody_builder.dynamic(channel=1, note=60, track=track, velocity=60)
        sum = 0
        for mes in track:
            sum += mes.time
        self.assertEqual(sum, time_limit * 2)

    def test_set_instrument(self):
        melody_builder = MelodyBuilder(outfile=MidiFile(), time_limit=120)
        track = MidiTrack()
        program_value = Instruments.Seashore
        melody_builder.set_instrument(track=track, channel=1, program_value=program_value)

        self.assertEqual(track[0].program, program_value)
