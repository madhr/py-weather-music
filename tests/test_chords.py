from unittest import TestCase

from music_rules.chords import Chords


class TestChords(TestCase):

    chords = Chords()

    def test_minor_triad(self):
        base_note = 10
        chord = self.chords.minor_triad(base_note)
        self.assertEqual(chord, [10, 13, 17])

    def test_major_triad(self):
        base_note = 10
        chord = self.chords.major_triad(base_note)
        self.assertEqual(chord, [10, 14, 17])

    def test_minor_seventh(self):
        base_note = 10
        chord = self.chords.minor_seventh(base_note)
        self.assertEqual(chord, [10, 13, 17, 20])

    def test_major_seventh(self):
        base_note = 10
        chord = self.chords.major_seventh(base_note)
        self.assertEqual(chord, [10, 14, 17, 20])
