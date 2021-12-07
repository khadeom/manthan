#works on local pc but not on colab
import speech_recognition as sr
import streamlit as st
# import scipy
# import soundfile as sf
r = sr.Recognizer()

def rec():
    with sr.Microphone() as source:
        # source =record(5)
        print("Speak Anything :")
        # audio = r.listen(source)
        audio= r.record(source,duration=4)
        with open("microphone-results.wav", "wb") as f:
            f.write(audio.get_wav_data())
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
        except:
            print("Sorry could not recognize what you said")

