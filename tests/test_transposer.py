from unittest import TestCase

from app.util.transposer import Transposer


class TestTransposer(TestCase):

    transposer = Transposer()

    def test_transpose(self):
        note = 10
        value = 5
        trasposed = self.transposer.transpose(note, value)
        self.assertEqual(trasposed, 15)

    def test_transpose_list(self):
        notes = [10, 12]
        value = 5
        transposed_list = self.transposer.transpose_list(notes, value)
        self.assertEqual(transposed_list, [15, 17])

    def test_octave_up(self):
        note = 10
        trasposed = self.transposer.octave_up(note)
        self.assertEqual(trasposed, 22)

    def test_octave_up_list(self):
        notes = [10, 12]
        transposed_list = self.transposer.octave_up_list(notes)
        self.assertEqual(transposed_list, [22, 24])

    def test_octave_down(self):
        note = 20
        trasposed = self.transposer.octave_down(note)
        self.assertEqual(trasposed, 8)

    def test_octave_down_list(self):
        notes = [20, 22]
        transposed_list = self.transposer.octave_down_list(notes)
        self.assertEqual(transposed_list, [8, 10])

    def test_two_octaves_up(self):
        note = 10
        trasposed = self.transposer.two_octaves_up(note)
        self.assertEqual(trasposed, 34)

    def test_two_octaves_up_list(self):
        notes = [20, 22]
        transposed_list = self.transposer.two_octaves_up_list(notes)
        self.assertEqual(transposed_list, [44, 46])

    def test_two_octaves_down(self):
        note = 34
        trasposed = self.transposer.two_octaves_down(note)
        self.assertEqual(trasposed, 10)

    def test_two_octaves_down_list(self):
        notes = [34, 36]
        transposed_list = self.transposer.two_octaves_down_list(notes)
        self.assertEqual(transposed_list, [10, 12])
