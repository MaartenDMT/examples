import os

import numpy as np
from pedalboard.pedalboard import Pedalboard
from pedalboard import Reverb, Distortion, Delay, NoiseGate, Compressor, LowShelfFilter, Gain
from pedalboard.io import AudioFile

# file_path = '/'
# file_directory = os.path.dirname(file_path)
# os.chdir(file_directory)


path_delay = os.path.normpath("audio/delay/nigero_delay.mp3")
path_distortion = os.path.normpath("audio/distortion/nigero_distortion.mp3")
path_reverb = os.path.normpath("audio/reverb/nigero_reverb.mp3")
path_mixed = os.path.normpath("audio/mixed/nigero_mixed.mp3")
path_podcast = os.path.normpath("audio/podcast/nigero_podcast.mp3")
print(os.path.abspath(path_mixed))

class Effect:
    def __init__(self)-> None:
        self.chunk_size = 500_000
        self.file_path = ""
        self.samplerate = ""
    
    def delay(self)-> None:
        self.check_path(self.file_path)
        with AudioFile(self.file_path) as f:
            self.samplerate = f.samplerate
            self.check_path(path_delay)
            with AudioFile(path_delay, "w", self.samplerate) as o:
                while f.tell() < f.frames:
                    audio = f.read(self.chunk_size) # => shape (2, 1_323_000)
                    mono = audio[0] # only one channel, (1_323_000)
                    delay_seconds = 0.2 # one fith of a second
                    delay_samples = int(f.samplerate * delay_seconds) 
                    volume = 0.75 # 75 percent of original volume
                    
                    for i in np.arange(len(mono)):
                        if i + delay_samples < len(mono):
                            mono[i + delay_samples] += mono[i] * volume
                            
                    delay_audio = mono
                    o.write(delay_audio)
    
    def distortion(self)-> None:
        self.check_path(self.file_path)
        with AudioFile(self.file_path) as f:
            self.check_path(path_distortion)
            with AudioFile(path_distortion, "w", self.samplerate) as o:
                while f.tell() < f.frames:
                    mono = f.read(self.chunk_size)[0]
                    gain = 200
                    volume = 0.010
                    mono = np.tanh(mono * gain) * volume
                    distorted_audio = mono
                    o.write(distorted_audio)
                    
    def reverb(self)-> None:
        self.check_path(self.file_path)
        with AudioFile(self.file_path) as f:
            self.samplerate = f.samplerate
            self.check_path(path_reverb)
            with AudioFile(path_reverb, "w", self.samplerate) as o:
                while f.tell() < f.frames:
                    audio = f.read(self.chunk_size)[0]
                    reverb = Reverb(room_size=0.45)
                    effected = reverb(audio, self.samplerate)
                    
                    o.write(effected)
    
    def mix(self)-> None:
        self.check_path(self.file_path)
        with AudioFile(self.file_path) as f:
            self.samplerate = f.samplerate
            self.check_path(path_mixed)
            with AudioFile(path_mixed, "w", self.samplerate) as o:
                while f.tell() < f.frames:
                    audio = f.read(self.chunk_size)[0]
                    board = Pedalboard([
                        Distortion(drive_db=25),
                        Delay(delay_seconds=0.6, feedback=0.5, mix=0.5),
                        Reverb(room_size=0.75),
                    ])
                    effected = board(audio, self.samplerate)
                    
                    o.write(effected)
    
    def podcast(self)-> None:
        self.check_path(self.file_path)
        with AudioFile(self.file_path) as f:
            self.samplerate = f.samplerate
            self.check_path(path_mixed)
            with AudioFile(path_podcast, "w", self.samplerate) as o:
                while f.tell() < f.frames:
                    audio = f.read(self.chunk_size)[0]
                    board = Pedalboard([
                        NoiseGate(threshold_db=-40, ratio=1.5, release_ms=250),
                        Compressor(threshold_db=-16, ratio=2.5),
                        LowShelfFilter(cutoff_frequency_hz=440, gain_db=10, q=1),
                        Gain(gain_db=6),
                    ])
                    effected = board(audio, self.samplerate)
                    
                    o.write(effected)
    
    @staticmethod
    def check_path(file_path)-> None:
        if not os.path.exists(file_path):
            print(f"Error: {file_path} does not exist.")
            return
        if not os.path.isfile(file_path):
            print(f"Error: {file_path} is not a file.")
            return
        if not os.access(file_path, os.W_OK):
            print(f"Error: {file_path} is not writable.")
            return