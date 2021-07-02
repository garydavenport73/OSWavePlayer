# WaveCLIPlayer
This is a simple wave player that uses the command line to issue instructions to the OS to play wav files.

I wanted to write the simplest cross-platform wav player, that can do the basics and would not have
any sort of dependencies.  It simply issues subprocess calls to the operating system to play the sound, and
as long as the operating system has not been significantly altered (you have not removed the operating systems
wave playing applications) it should work.  The player issues commands to stop the subprocesses to stop playing
the sounds.

#### -Windows10 uses the Media.Soundplayer module built into Windows 10

#### -Linux uses ALSA which is part of the Linux kernel since version 2.6 and later

#### -MacOS uses the afplay module which is present OS X 10.5 and later`

To use the module simply add:
```
from wavecliplayer import *`
```
and this will import all its functions.

The module essentially contains 3 functions:
```
playwave("yourfilename")

stopwave(yourSound)

getIsPlaying(yourSound)
```
Here are some examples on how to use them.
Note that with 'playwave' it can be used as a standalone function, but if you want to stop the file from playing,
you will have to use the return value of playwave.  Read a little further and the examples should be obvious.

### Examples:

To play a wave file:
```
playwave("coolhipstersong.wav") #-> this plays the wav file

mysong=play("coolhipstersong.wav") #-> this plays the wav file and also returns the song subprocess
```

To stop your song:
```
stopwave(mysong) # -> this stops the subprocess, mysong, which you created in the line above
```

To find out if your wave file is playing:

```
isitplaying = getIsPlaying(mysong) -> sets a variable to True or False, depending on if process is running

print(getIsPlaying(mysong)) -> prints True or False depending on if process is running

if getIsPlaying(mysong)==True:
    print("Yes, your song is playing")
else:
    print("Your song is not playing")
```

To play a wave file synchronously:
```
playwave("coolhipstersong.wav",1) #-> this plays the wav file synchronously

or

playwave("coolhipstersong.wav",block=True)


* Note: commands below will work, but you cannot stop the song, because your progam will be blocked until the song is done playing

mysong=play("coolhipstersong.wav",1) #-> this plays the wav file synchronously and also returns the song subprocess
or 
mysong=play("coolhipstersong.wav",block=True) #-> this plays the wav file synchronously and also returns the song subprocess


```

### Notes about using this module as a replacement in the playsound module:

You can replace the words 'playwave' with 'playsound', and the module will work as intended but still only works for wav files.

I included this feature so these functions could be used as a replacement for playsound function found in the playsound module at https://github.com/TaylorSMarks/playsound/blob/master/playsound.py.  The only caveat is that the default
behaviour is to NOT block in my program (my function plays asynchronously by default).  The playsound module's function 'playsound' has its
default behaviour to block = True (it plays synchronously by default).  

So I you are using this as a replacement because the playsound module was not working for you (as it is no longer maintained), you may have to specify the second argument, block, and set it explicitly.  

In other words for backwards compatibility (wav files only) you can replace the code:
```
playsound("yourwavefile.wav") 

with

playsound("yourwavefile.wav",1)
or
playsound("yourwavefile.wav", block=true)
```
for backwards compatibility for wav files.

If you'd rather you can go to the source file 'wavecliplayer.py' you can simply change the phrases from block=False to block=True and you will get the original behaviour.  I did not want to keep the default as blocking because its unusual for me use this function in this manner.  

Normally, when I am playing a sound in a program I have written, I do not want the entire program to halt when the sound plays, so I simply could not bring myself to keep this as the default behaviour.  But this is truely just a matter of preference.

