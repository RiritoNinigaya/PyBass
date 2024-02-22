// dllmain.cpp : Defines the entry point for the DLL application.
#include "includes.hpp"
#include <iostream>
#define PYTHON_DLLEXPORT extern "C" __declspec(dllexport)
PYTHON_DLLEXPORT void PlayMusicInBass(const char* filename) 
{
    Bass::BASS_Start();
    if (Bass::BASS_Init(-1, 48000, 0, 0, 0)) {
        Bass::HSTREAM stream_line = Bass::BASS_StreamCreateFile(false, (const WCHAR*)filename, 0, 0, BASS_SAMPLE_LOOP);
        if (stream_line) 
        {
            Bass::BASS_ChannelPlay(stream_line, true);
        }
    }
}
PYTHON_DLLEXPORT void StopBass() {
    if (Bass::BASS_Free()) {
        Bass::BASS_Stop();
    }
    else {
        MessageBoxA(0, "PyBass Library Is Failing To Stoping This Music", "Library for BASS(Python Language)", MB_OK | MB_ICONERROR);
    }

}
BOOL APIENTRY DllMain( HMODULE hModule,
                       DWORD  ul_reason_for_call,
                       LPVOID lpReserved
                     )
{
    switch (ul_reason_for_call)
    {
    case DLL_PROCESS_ATTACH:
        MessageBoxA(0, "Attached!!!", "PyBass", MB_OK | MB_ICONWARNING);
    case DLL_THREAD_ATTACH:
    case DLL_THREAD_DETACH:
    case DLL_PROCESS_DETACH:
        break;
    }
    return TRUE;
}

