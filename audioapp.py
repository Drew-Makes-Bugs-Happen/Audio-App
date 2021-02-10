
from ctypes import *


vmapi = cdll.LoadLibrary("C:\Program Files (x86)\VB\Voicemeeter\VoicemeeterRemote64.dll")

for thing in vmapi:
    print(thing)
