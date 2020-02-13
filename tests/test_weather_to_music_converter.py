from unittest import TestCase

from mido import MidiTrack, Message, MidiFile

from build_midi.weather_to_music_converter import WeatherToMusicConverter


class TestWeatherToMusicConverter(TestCase):

    music_converter = WeatherToMusicConverter()

    def test_weather_to_music(self):
        api_key = '7f1f66212a27b1173d1c96f3f644b3a5'
        city = 'london,uk'
        outfile = self.music_converter.weather_to_music(api_key, city)
        self.assertIsInstance(outfile, MidiFile)

    def test_weather_to_music_bad_api_key(self):
        api_key = 'bad_key'
        city = 'london,uk'
        with self.assertRaises(Exception) as ex:
            self.music_converter.weather_to_music(api_key, city)
        self.assertEqual("Failed to pull weather forecast", str(ex.exception))

    def test_weather_to_music_bad_city(self):
        api_key = '7f1f66212a27b1173d1c96f3f644b3a5'
        city = 'abcd,ef'
        with self.assertRaises(Exception) as ex:
            self.music_converter.weather_to_music(api_key, city)
        self.assertEqual("Failed to pull weather forecast", str(ex.exception))


    def test_get_midi_track_time(self):
        track = MidiTrack()
        time = 100
        track.append(Message('note_on', note=60, channel=1, velocity=60, time=time))
        track.append(Message('note_off', note=60, channel=1, velocity=60, time=time))

        self.assertEqual(self.music_converter.get_midi_track_time(track), time * 2)
