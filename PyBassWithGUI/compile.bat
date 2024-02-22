@echo off

pyinstaller Main.py --windowed --add-binary="PyBass_Cpp.dll":"PyBass_Cpp.dll" --collect-binaries "PyBass_Cpp.dll" --name "PyBassGUI" --onefile