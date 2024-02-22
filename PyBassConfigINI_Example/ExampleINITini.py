import configparser # For Initializating INI File
import os
import sys
import ctypes
import time
configpars = configparser.ConfigParser()
kernel32_dll = ctypes.CDLL("Kernel32.dll")
def ReadConf():
    return configpars.read(os.getcwd() + "\\Configuration\\conf.ini")
def LoadPyBass():
    pybass_lib = ctypes.cdll.LoadLibrary(os.getcwd() + "\\PyBass_Cpp.dll")
    return pybass_lib
def SetConsoleTitle(titlename : str):
    return kernel32_dll.SetConsoleTitleW(titlename)
def Main():
    library_p = LoadPyBass()
    ReadConf()
    SetConsoleTitle("PyBassConfigINI by RiritoNinigaya")
    library_p.PlayMusicInBass(configpars['Config']['Output'])
    while True:
        time.sleep(6)

if __name__ == "__main__":
    Main()
