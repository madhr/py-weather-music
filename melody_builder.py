import random
from arpeggiator import Arpeggiator
from mido import Message, MidiTrack


class MelodyBuilder:


	def random(self, outfile, program_value, channel, scale, time_limit):
		track = MidiTrack()
		outfile.tracks.append(track)
		track.name = 'random_scale'
		track.append(Message('program_change', channel=channel, program=program_value, time=0))
		sum = 0
		while sum < time_limit:
			note = random.choice(scale)
			time = random.randrange(120, 600, 60)
			sum += time
			track.append(Message('note_on', note=note, channel=channel, velocity=60, time=time))
			track.append(Message('note_off', note=note, channel=channel, velocity=60, time=time))
		return outfile

	def arpeggiator(self, outfile, program_value, channel, pattern, scale, time_limit):
		track1 = MidiTrack()
		outfile.tracks.append(track1)
		track1.name = "arp"
		track1.append(Message('program_change', channel=channel, program=program_value, time=0))
		arpeggiator = Arpeggiator()
		arp_up_and_down = arpeggiator.create(pattern, scale)
		count = 0
		notes_size = len(arp_up_and_down)
		sum = 0
		while sum < time_limit:
			if count == notes_size:
				count = 0
			note = arp_up_and_down[count]
			count = count + 1
			time = 150
			sum += time
			track1.append(Message('note_on', note=note, channel=channel, velocity=60, time=time))
			track1.append(Message('note_off', note=note, channel=channel, velocity=60, time=time))
		return outfile
