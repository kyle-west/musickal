from Musickal import *
import random

m = Musickal()

MEASURE_LENGTH = 2
TIMES = [ .5, 1.0, 1.5, 2.0 ]
TIMES_length = len(TIMES)
print("TIMES: ({}, {})".format(0, TIMES_length), TIMES)

CMS = SCALES["C-Major"][slice(20, -20)]
CMS_length = len(CMS)
print("CMS: ({}, {})".format(0, CMS_length), CMS)


song = []

def selectNote (c, t, scaleNotes = CMS):
  note = (scaleNotes[c], t)
  return note

def sample (i, minVal, maxVal, jump = 1, entropy = 100, sustainable = False):
  if ((random.random() * entropy) > entropy/(len(song) + 1)):
    direction = (-1)**(int(random.random() * entropy))
    x = i + direction*jump
    if x > maxVal or x < minVal: 
      x = i - direction*jump
    return x
  else :
    return i

def sampleMeasureTimes(length, slots):
  t = length/4
  return [t,t,t,t]

def createMeasure ():
  measure = []
  c , t = int(random.random() * CMS_length), int(random.random() * TIMES_length) 
  jump_c = int(random.random() * 8)
  for t in sampleMeasureTimes(MEASURE_LENGTH, 4):
    c = sample(c, 0, CMS_length - 1, jump_c)
    measure.append(selectNote(c, t))
  print(measure)
  return measure



print("----------------------------------------------------------------------")
for i in range(0, 12):
  song += createMeasure()


print("----------------------------------------------------------------------")
print(song)
m.playSong(song)