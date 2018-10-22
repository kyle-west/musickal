# Setup

Install dependencies:
```sh
brew install portaudio
pip install pyaudio
```

# Notes

To install all the notes, it is easiest to include the whole library.

```python
from Musickal import *
```

Here is a reference to the notes we allow for (arranged to match the 4th octave 
on the piano):
```
  Db   Eb        Gb   Ab   Bb
C    D    E    F    G    A    B
```

Note that half steps are annotated as flats instead of sharps. This is because `#`
is reserved in python for comments, where `b` is simply a letter. 

To specify an octave of a note, postfix it with the octave number:

```
...   Db3  Eb3       Gb3  Ab3  Bb3      Db4  Eb4       Gb4  Ab4  Bb4   ...
    C3   D3   E3   F3   G3   A3   B3  C4   D4   E4   F4   G4   A4   B4
```

# Play the audio

Here is an example of how to play notes:

```python
from Musickal import *

m = Musickal()

duration = .25

m.playSong([
  (B, duration),
  (A, duration), 
  (D, duration), 
  (C, duration), 
  (A, duration), 
  (F, duration), 
  (E, duration)
])
```