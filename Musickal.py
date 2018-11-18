import pyaudio
import numpy as np

class Musickal:
  def __init__(self, volume = 1.0):
    self.player = pyaudio.PyAudio()
    self.volume = volume 
    self.fs     = 44100
  
  def playNote (self, f, duration):
    song = self.player.open(
      format=pyaudio.paFloat32, channels=1, rate=self.fs, output=True
    )
    samples = self.generateSample(f, duration)
    song.write(self.volume * samples)
    song.stop_stream()
    song.close()

  def generateSample(self, f, duration):
    return (np.sin(2 * np.pi * np.arange(self.fs * duration) * f / self.fs)).astype(np.float32)

  def playSong(self, notes):
    song = self.player.open(
      format=pyaudio.paFloat32, channels=1, rate=self.fs, output=True
    )

    for note in notes:
      samples = self.generateSample(note[0], note[1])
      song.write(self.volume * samples)

    song.write(self.volume * samples)
    song.stop_stream()
    song.close()
  
  def __del__(self):
    self.player.terminate()

## ---------------------------- NOTES ----------------------------- ##

__whole_notes = np.array([
  261.63,
  293.66,
  329.63,
  349.23,
  392.00,
  440.00,
  493.88
])

C, D, E, F, G, A, B = __whole_notes*1.0

C0, D0, E0, F0, G0, A0, B0 = __whole_notes/16.0
C1, D1, E1, F1, G1, A1, B1 = __whole_notes/8.0
C2, D2, E2, F2, G2, A2, B2 = __whole_notes/4.0
C3, D3, E3, F3, G3, A3, B3 = __whole_notes/2.0
C4, D4, E4, F4, G4, A4, B4 = __whole_notes*1.0
C5, D5, E5, F5, G5, A5, B5 = __whole_notes*2.0
C6, D6, E6, F6, G6, A6, B6 = __whole_notes*4.0
C7, D7, E7, F7, G7, A7, B7 = __whole_notes*8.0
C8, D8, E8, F8, G8, A8, B8 = __whole_notes*16.0

__half_notes = np.array([
  277.18,
  311.13,
  369.99,
  415.30,
  466.16
])

Db, Eb, Gb, Ab, Bb = __half_notes*1.0

Db0, Eb0, Gb0, Ab0, Bb0 = __half_notes/16.0
Db1, Eb1, Gb1, Ab1, Bb1 = __half_notes/8.0
Db2, Eb2, Gb2, Ab2, Bb2 = __half_notes/4.0
Db3, Eb3, Gb3, Ab3, Bb3 = __half_notes/2.0
Db4, Eb4, Gb4, Ab4, Bb4 = __half_notes*1.0
Db5, Eb5, Gb5, Ab5, Bb5 = __half_notes*2.0
Db6, Eb6, Gb6, Ab6, Bb6 = __half_notes*4.0
Db7, Eb7, Gb7, Ab7, Bb7 = __half_notes*8.0
Db8, Eb8, Gb8, Ab8, Bb8 = __half_notes*16.0


## ---------------------------- SCALES ----------------------------- ##

SCALES = {
  "B-Major": [
    B0, Db0, Eb0, E0, Gb0, Ab1, Bb1,
    B1, Db1, Eb1, E1, Gb1, Ab2, Bb2,
    B2, Db2, Eb2, E2, Gb2, Ab3, Bb3,
    B3, Db3, Eb3, E3, Gb3, Ab4, Bb4,
    B4, Db4, Eb4, E4, Gb4, Ab5, Bb5,
    B5, Db5, Eb5, E5, Gb5, Ab6, Bb6,
    B6, Db6, Eb6, E6, Gb6, Ab7, Bb7,
    B7, Db7, Eb7, E7, Gb7, Ab8, Bb8,
    B8, Db8, Eb8, E8, Gb8
  ],
  "C-Major": [
    C0, D0, E0, F0, G0, A0, B0,
    C1, D1, E1, F1, G1, A1, B1,
    C2, D2, E2, F2, G2, A2, B2,
    C3, D3, E3, F3, G3, A3, B3,
    C4, D4, E4, F4, G4, A4, B4,
    C5, D5, E5, F5, G5, A5, B5,
    C6, D6, E6, F6, G6, A6, B6,
    C7, D7, E7, F7, G7, A7, B7,
    C8, D8, E8, F8, G8, A8, B8
  ]
}