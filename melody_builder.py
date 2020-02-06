import random
from arpeggiator import Arpeggiator
from mido import Message, MidiTrack, MidiFile

from util.chords import Chords


class MelodyBuilder:

	outfile: MidiFile
	time_limit: int

	def __init__(self, outfile, time_limit):
		self.outfile = outfile
		self.time_limit = time_limit


	def random(self, program_value, channel, scale):
		track = MidiTrack()
		self.outfile.tracks.append(track)
		track.name = 'random_scale'
		track.append(Message('program_change', channel=channel, program=program_value, time=0))
		sum = 0
		while sum < self.time_limit:
			note = random.choice(scale)
			time = random.randrange(120, 600, 60)
			sum += time
			track.append(Message('note_on', note=note, channel=channel, velocity=60, time=time))
			track.append(Message('note_off', note=note, channel=channel, velocity=60, time=time))
		return self.outfile

	def arpeggiator(self, program_value, channel, pattern, scale):
		track = MidiTrack()
		self.outfile.tracks.append(track)
		track.name = "arp"
		track.append(Message('program_change', channel=channel, program=program_value, time=0))
		arpeggiator = Arpeggiator()
		arp_up_and_down = arpeggiator.create(pattern, scale)
		count = 0
		notes_size = len(arp_up_and_down)
		sum = 0
		while sum < self.time_limit:
			if count == notes_size:
				count = 0
			note = arp_up_and_down[count]
			count = count + 1
			time = 150
			sum += time
			track.append(Message('note_on', note=note, channel=channel, velocity=60, time=time))
			track.append(Message('note_off', note=note, channel=channel, velocity=60, time=time))
		return self.outfile

	def chords(self, program_value, channel, base_note):
		track = MidiTrack()
		self.outfile.tracks.append(track)
		track.name = "chords"
		track.append(Message('program_change', channel=channel, program=program_value, time=0))
		chords = Chords()
		chord = chords.minor_seventh(base_note)
		sum = 0
		while sum < self.time_limit:
			time = 300
			sum += time
			for note in chord:
				note_time = time if note == base_note else 0
				track.append(Message('note_on', note=note, channel=channel, velocity=60, time=note_time))
			for note in chord:
				note_time = time if note == base_note else 0
				track.append(Message('note_off', note=note, channel=channel, velocity=60, time=note_time))

		return self.outfile
