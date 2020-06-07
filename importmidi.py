from mingus.midi import fluidsynth
from mingus.containers import NoteContainer, Note
import mingus.midi.fluidsynth
from mingus.midi import midi_file_in
from mingus.midi import midi_file_out
from mingus.extra import lilypond as lp
import time
import sys
from random import random
import os.path

(m, bpm) = midi_file_in.MIDI_to_Composition("sample/MIDI/PIrate.mid")
midi_file_out.write_Composition("test.mid", m, bpm)

exportpdf = lp.from_Composition(m)
lp.to_png(exportpdf, "PirateTest")

print("TEST")
