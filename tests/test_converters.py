from unittest import TestCase

from build_midi.converters import Converter
from weather.weather_forecast import *


class TestConverter(TestCase):

    converter = Converter()

    def test_music_notes_to_sequence_length(self):
        list_of_notes = [1, 2, 3, 4]
        length = 6
        seq_length = self.converter.music_notes_to_sequence_length(list_of_notes, length)
        self.assertEqual(seq_length, [1, 2, 3, 4, 13, 14])

    def test_amplitude_to_arp_pattern(self):
        list_of_notes = [1, 2, 3, 4]
        amplitude = 2
        pattern = self.converter.amplitude_to_arp_pattern(amplitude, list_of_notes)
        self.assertEqual(pattern, [1, 2, 3, 4, 13, 14, 15, 16, 13, 14, 15, 16, 15, 14, 13, 16, 15, 14, 13, 4, 3, 2])

    def test_temperature_to_base_note(self):
        feels_like = 276.35
        base_note = self.converter.temperature_to_base_note(feels_like)
        self.assertEqual(base_note, 59)

    def test_rain_to_scale_size(self):
        rain = 23.5
        scale = [1, 2, 3, 4]
        scale_size = self.converter.rain_to_scale_size(rain, scale)
        self.assertEqual(len(scale_size), 4)

    def test_clouds_to_chord_length(self):
        clouds = 30
        length = self.converter.clouds_to_chord_length(clouds)
        self.assertEqual(length, 360)

    def test_humidity_to_velocity(self):
        humidity = 40
        velocity = self.converter.humidity_to_velocity(humidity)
        self.assertEqual(velocity, 50)

    def test_wind_to_velocity(self):
        wind = 22.6
        velocity = self.converter.wind_to_velocity(wind)
        self.assertEqual(velocity, 113)


    def test_average_temperature(self):
        temperature1 = Temperature(276.5, 277.4, 267.2, 256.4)
        pressure1 = Pressure(1023, 1022)
        weather1 = Weather(57, 24, 22.5, 1.2)
        temperature2 = Temperature(267.4, 278.4, 263.5, 233.4)
        pressure2 = Pressure(1023, 1022)
        weather2 = Weather(57, 24, 22.5, 1.2)
        timestamp1 = WeatherTimestamp(temperature1, pressure1, weather1, 100000)
        timestamp2 = WeatherTimestamp(temperature2, pressure2, weather2, 100010)
        weather_timestamps = [timestamp1, timestamp2]
        avg_temp = self.converter.average_temperature(weather_timestamps)
        self.assertAlmostEqual(avg_temp, 244.9)

    def test_average_temperature_to_ticks_per_beat(self):
        average_temperature = 277.4
        ticks_per_beat = self.converter.average_temperature_to_ticks_per_beat(average_temperature)
        self.assertEqual(ticks_per_beat, 390)
