import math

import numpy as np
import wave
import matplotlib.pyplot as plt
from  scipy import signal
from scipy.io import loadmat
import scipy.io.wavfile as wav
import scipy.io.wavfile


tu = wave.open('te4.wav','r')
#tu = scipy.io.wavfile.read('te4.wav')