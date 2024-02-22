import ctypes
import os
import time
def InitLib():
    librarypybass = ctypes.cdll.LoadLibrary("{}".format(os.getcwd() + "\\PyBass_Cpp.dll"))
    return librarypybass
def Main():
    InitLib().PlayMusicInBass("{}".format(os.getcwd() + "\\Horizon.mp3"))
    while True:
        time.sleep(4)
if __name__ == "__main__":
    Main()