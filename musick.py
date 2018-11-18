from Musickal import *
import random

m = Musickal()

MEASURE_LENGTH = 4
TIMES = [ .5, 1.0, 1.5, 2.0 ]
TIMES_length = len(TIMES)
print("TIMES: ({}, {})".format(0, TIMES_length), TIMES)

SCALE = SCALES["C-Major"][slice(20, -20)]
SCALE_length = len(SCALE)
print("SCALE: ({}, {})".format(0, SCALE_length), SCALE)

def selectNote (c, t):
  return (SCALE[c], t)

def sample (i, minVal, maxVal, jump = 1, entropy = 100):
  direction = (-1)**(int(random.random() * entropy))
  x = i + direction*jump
  if x > maxVal or x < minVal: 
    x = i - direction*jump
  return x

def sampleMeasureTimes(length, slots):
  portion_size = length / slots
  times = []
  t = 0
  for i in range(0, slots):
    t += portion_size
    if (random.random() * 100) > 50:
      times.append(t)
      t = 0
  if t > 0:
      times.append(t)
  return times

def createMeasure (times):
  measure = []
  c = int(random.random() * SCALE_length)
  jump_c = int(random.random() * 5 + 1)
  for t in times:
    c = sample(c, 0, SCALE_length - 1, jump_c)
    measure.append(selectNote(c, t))
  print(measure)
  return measure



print("----------------------------------------------------------------------")
song = []
for i in range(0, 24):
  if i % 4 == 0:
    times = sampleMeasureTimes(MEASURE_LENGTH, 8)
  song += createMeasure(times)


print("----------------------------------------------------------------------")
print(song)
m.playSong(song)