from unittest import TestCase

from app.util.arp_pattern import ArpPattern
from app.util.arpeggiator import Arpeggiator


class TestArpeggiator(TestCase):

    arpeggiator = Arpeggiator()

    def test_create_up_and_down(self):
        list_of_notes = [1, 2, 3, 4]
        pattern = self.arpeggiator.create(ArpPattern.UP_AND_DOWN, list_of_notes)
        self.assertEqual(pattern, [1, 2, 3, 4, 3, 2])

    def test_create_up(self):
        list_of_notes = [1, 2, 3, 4]
        pattern = self.arpeggiator.create(ArpPattern.UP, list_of_notes)
        self.assertEqual(pattern, [1, 2, 3, 4])

    def test_create_down(self):
        list_of_notes = [1, 2, 3, 4]
        pattern = self.arpeggiator.create(ArpPattern.DOWN, list_of_notes)
        self.assertEqual(pattern, [4, 3, 2, 1])

    def test_create_up_and_down_2_octaves(self):
        list_of_notes = [1, 2, 3, 4]
        pattern = self.arpeggiator.create(ArpPattern.UP_AND_DOWN_2_OCTAVES, list_of_notes)
        self.assertEqual(pattern, [1, 2, 3, 4, 13, 14, 15, 16, 15, 14, 13, 4, 3, 2])

    def test_create_up_2_octaves(self):
        list_of_notes = [1, 2, 3, 4]
        pattern = self.arpeggiator.create(ArpPattern.UP_2_OCTAVES, list_of_notes)
        self.assertEqual(pattern, [1, 2, 3, 4, 13, 14, 15, 16])

    def test_create_down_2_octaves(self):
        list_of_notes = [1, 2, 3, 4]
        pattern = self.arpeggiator.create(ArpPattern.DOWN_2_OCTAVES, list_of_notes)
        self.assertEqual(pattern, [16, 15, 14, 13, 4, 3, 2, 1])




