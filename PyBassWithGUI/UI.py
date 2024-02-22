import dearpygui.dearpygui as dpg
import ctypes as c
import os

def GetPyBassLib():
    library_pybass = c.cdll.LoadLibrary(os.getcwd() + "\\PyBass_Cpp.dll")
    return library_pybass
def MainUI():
    dpg.create_context()

    with dpg.window(label="PyBass GUI by DarknessSoul", tag="WindowPYBASS"):
        dpg.add_input_text(label="Path to Music", tag="PATH_PYBASS")
        dpg.add_button(label="Play Music", callback=PlayMusic)
        dpg.add_button(label="Stop Music", callback=StopMusic)
    dpg.create_viewport(title='PyBass GUI by RiritoNinigaya', width=455, height=455)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("WindowPYBASS", True)
    dpg.start_dearpygui()
    dpg.destroy_context()
def PlayMusic():
    return GetPyBassLib().PlayMusicInBass(dpg.get_value("PATH_PYBASS"))
def StopMusic():
    return GetPyBassLib().StopBass()
