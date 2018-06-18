import os
import subprocess
from gtts import gTTS

def speech_output(out_speech):
    tts = gTTS(text=out_speech, lang="en")
    tts.save("out.mp3")
    try:
        subprocess.Popen(["mpg123", "-q", "out.mp3"]).wait()
    except OSError as e:
        if e.errno == os.errno.ENOENT:
            print("You need to install mpg123 for this program to run")
        else:
            raise
