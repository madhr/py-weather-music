from unittest import TestCase

from music_rules.music_scale import MusicScale


class TestMusicScale(TestCase):

    music_scale = MusicScale()

    def test_pentatonic(self):
        note = 10
        scale = self.music_scale.pentatonic(note)
        self.assertEqual(scale, [10, 13, 15, 17, 20])

    def test_melodic_minor(self):
        note = 10
        scale = self.music_scale.melodic_minor(note)
        self.assertEqual(scale, [10, 12, 13, 15, 17, 18, 21])

    def test_minor(self):
        note = 10
        scale = self.music_scale.minor(note)
        self.assertEqual(scale, [10, 12, 13, 15, 17, 18, 20])

    def test_major(self):
        note = 10
        scale = self.music_scale.major(note)
        self.assertEqual(scale, [10, 12, 14, 15, 17, 19, 21])
