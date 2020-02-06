from mido import MidiFile
from pathlib import Path
from util import instruments
import weather_api
from arpeggiator import ArpPattern
from util.chords import Chords
from melody_builder import MelodyBuilder

if __name__ == '__main__':

	# get weather from api and parse it

	API_KEY = '7f1f66212a27b1173d1c96f3f644b3a5'
	city = 'Wroclaw,pl'

	api_handling = weather_api.WeatherApi()

	json_weather_forecast = api_handling.get_json_weather_forecast_from_api(city, API_KEY)

	if json_weather_forecast is None:
		raise Exception("Failed to pull weather forecast")

	weather_forecast = api_handling.parse_weather_forecast(json_weather_forecast)

	print("Weather forecast successfully parsed")

	# create and save midi file

	outfile = MidiFile()
	melody_builder = MelodyBuilder()
	chords = Chords()

	SONG_LENGTH = 100000
	base_note = 60

	outfile = melody_builder.random(
		outfile=outfile,
		program_value=instruments.Instruments.Celesta.value,
		channel=0,
		scale=chords.minor_seventh(base_note),
		time_limit=SONG_LENGTH
	)

	outfile = melody_builder.arpeggiator(
		outfile=outfile,
		program_value=instruments.Instruments.Piccolo.value,
		channel=1,
		pattern=ArpPattern.UP,
		scale=chords.minor_triad(base_note),
		time_limit=SONG_LENGTH
	)

	outfile = melody_builder.chords(
		outfile=outfile,
		program_value=instruments.Instruments.Piccolo.value,
		channel=2,
		base_note=base_note-12,
		time_limit=SONG_LENGTH
	)

	file_dir = 'midi_out'
	file_name = 'song-for-'+city+'.mid'
	Path(file_dir).mkdir(exist_ok=True)
	outfile.save(file_dir+'/'+file_name)
	print("file saved at "+file_dir+'/'+file_name)
