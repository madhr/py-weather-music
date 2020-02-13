import random
from music_rules.arpeggiator import Arpeggiator
from mido import Message, MidiFile


class MelodyBuilder:

	outfile: MidiFile
	time_limit: int

	def __init__(self, outfile, time_limit):
		self.outfile = outfile
		self.time_limit = time_limit

	def random(self, channel, scale, track, time_factor = 60):

		sum = 0
		while sum < self.time_limit and not scale is None:
			note = random.choice(scale)
			time = abs(random.randrange(2*time_factor, 8*time_factor, time_factor))

			if (sum + time >= self.time_limit):
				time = self.time_limit - sum
				sum = self.time_limit
			else:
				sum += time
			track.append(Message('note_on', note=note, channel=channel, velocity=60, time=time))
			track.append(Message('note_off', note=note, channel=channel, velocity=60, time=time))

		# fill with empty
		remaining_time = int(self.time_limit - sum)
		track.append(Message('note_on', note=0, channel=channel, velocity=0, time=remaining_time))
		track.append(Message('note_off', note=0, channel=channel, velocity=0, time=remaining_time))

		return self.outfile

	def arpeggiator(self, channel, pattern, track, time_factor, scale, velocity = 60):

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
			sum += time_factor
			track.append(Message('note_on', note=note, channel=channel, velocity=velocity, time=time_factor))
			track.append(Message('note_off', note=note, channel=channel, velocity=velocity, time=time_factor))
		return self.outfile

	def chord(self, channel, chord, track, time_factor = 60):

		sum_of_times = 0

		for note in chord:
			note_time = time_factor if note == chord[0] else 0
			sum_of_times += note_time
			track.append(Message('note_on', note=note, channel=channel, velocity=60, time=note_time))
		for note in chord:
			note_time = time_factor if note == chord[0] else 0
			sum_of_times += note_time
			track.append(Message('note_off', note=note, channel=channel, velocity=60, time=note_time))

		remaining_time = int(self.time_limit - sum_of_times / 2)
		track.append(Message('note_on', note=0, channel=channel, velocity=0, time=remaining_time))
		track.append(Message('note_off', note=0, channel=channel, velocity=0, time=remaining_time))

		return self.outfile

	def dynamic(self, channel, note, track, velocity):

		track.append(Message('note_on', note=note, channel=channel, velocity=velocity, time=self.time_limit))
		track.append(Message('note_off', note=note, channel=channel, velocity=velocity, time=self.time_limit))

		return self.outfile

	def set_instrument(self, track, channel, program_value):
		track.append(Message('program_change', channel=channel, program=program_value, time=0))
		return track