import speech_recognition as sr

def speech_input():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = r.listen(source)
        print("Got the speech. Now processing...")

    # recognize speech using Wit.ai
    # Add your API key to a '.keys' file in the root of the project
    WIT_AI_KEY = ""
    with open(".keys", "r") as keys:
        WIT_AI_KEY = keys.readline().strip()
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

    return in_speech
