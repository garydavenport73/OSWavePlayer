#   Gary Davenport, WavCLIPlayer functions 6/2/2021
#
#   plays wav files using native wav playing command line interface calls
#   for Windows 10, Linux, and MacOS
#
#   Windows10 uses the Media.Soundplayer module built into Windows 10
#   Linux uses ALSA which is part of the Linux kernel since version 2.6 and later
#   MacOS uses the afplay module which is present OS X 10.5 and later
#   

from platform import system
import subprocess
from subprocess import Popen, PIPE
from os import path

def playwave(fileName, block=False):
    fileName=fileName
    if system()=="Linux": command = "exec aplay --quiet " + path.abspath(fileName)
    elif system()=="Windows": command="%SystemRoot%\system32\WindowsPowerShell/v1.0\powershell.exe -c (New-Object Media.SoundPlayer '"+path.abspath(fileName)+"').PlaySync()"
    elif system()=="Darwin": command = "exec afplay \'" + path.abspath(fileName)+"\'"
    else: print(str(system()+" unknown to wavecliplayer"));return None
    if block==True: P = subprocess.Popen(command, universal_newlines=True, shell=True,stdout=PIPE, stderr=PIPE).communicate()
    else: P = subprocess.Popen(command, universal_newlines=True, shell=True,stdout=PIPE, stderr=PIPE)
    return P

def stopwave(process):
    try:
        if process is not None:
            if system()=="Windows": subprocess.call(['taskkill', '/F', '/T', '/PID',  str(process.pid)])
            else: process.terminate()
    except:
        pass

def getIsPlaying(process):
    isSongPlaying=False
    if process is not None:
        try: return(process.poll() is None)
        except: pass
    return isSongPlaying

playsound=playwave
stopsound=stopwave
