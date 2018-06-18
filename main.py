import speech_recognition as sr
import os
import subprocess
from gtts import gTTS

r = sr.Recognizer()

with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)
    print("Say something!")
    audio = r.listen(source)
    print("Got the speech. Now processing...")

# recognize speech using Wit.ai
WIT_AI_KEY = ""
with open(".keys", "r") as keys:
    WIT_AI_KEY = file.readline().strip()
if not WIT_AI_KEY:
    print("API key not available")
    exit()

in_speech = ""
try:
    in_speech = r.recognize_wit(audio, key=WIT_AI_KEY)
    print("You said " + in_speech)
except sr.UnknownValueError:
    print("Wit.ai could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Wit.ai service; {0}".format(e))

if (in_speech):
    tts = gTTS(text=in_speech, lang="en")
    tts.save("out.mp3")
    subprocess.Popen(["mpg123", "-q", "out.mp3"]).wait()
