import pyaudio
import audioop
import math

p = pyaudio.PyAudio()
stream = p.open(format = pyaudio.paInt16,
             channels = 1,
             rate = 48000,
             input = True,
             frames_per_buffer = 2048)
while 1:
 data = stream.read(2048)
 rms = audioop.rms(data,2)
 print(rms)
 decibel = 20* math.log10(rms)
 print(decibel)

