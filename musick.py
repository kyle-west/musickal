from Musickal import *
import random

m = Musickal()

MEASURE_LENGTH = 4
TIMES = [ .5, 1.0, 1.5, 2.0 ]
TIMES_length = len(TIMES)
print("TIMES: ({}, {})".format(0, TIMES_length), TIMES)

CMS = SCALES["C-Major"][slice(20, -20)]
CMS_length = len(CMS)
print("CMS: ({}, {})".format(0, CMS_length), CMS)



def selectNote (c, t):
  return (CMS[c], t)

def sample (i, minVal, maxVal, jump = 1, entropy = 100):
  direction = (-1)**(int(random.random() * entropy))
  x = i + direction*jump
  if x > maxVal or x < minVal: 
    x = i - direction*jump
  return x

def sampleMeasureTimes(length, slots):
  t = length / slots
  return [t,t,t,t]

def createMeasure ():
  measure = []
  c = int(random.random() * CMS_length)
  jump_c = int(random.random() * 5 + 1)
  for t in sampleMeasureTimes(MEASURE_LENGTH, 4):
    c = sample(c, 0, CMS_length - 1, jump_c)
    measure.append(selectNote(c, t))
  print(measure)
  return measure



print("----------------------------------------------------------------------")
song = []
for i in range(0, 24):
  song += createMeasure()


print("----------------------------------------------------------------------")
print(song)
m.playSong(song)