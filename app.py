
import streamlit as st
from questions import qna
# import pandas as pd
import re
import random
from datetime import datetime
import time
import speech_recognition as sr
import pyttsx3

# import scipy
# import soundfile as sf
r = sr.Recognizer()

def rec(count):
    with sr.Microphone() as source:
        # source =record(5)
        print("Speak Anything :")
        # audio = r.listen(source)
        audio= r.record(source,duration=6)
        name="ans"+str(count)+".wav"
        '''
        with open(name, "wb") as f:
            f.write(audio.get_wav_data())
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
        except:
            print("Sorry could not recognize what you said")
         '''
    return count+1


def tts(reply_string):
    engine = pyttsx3.init()
    engine.say(reply_string)  
    engine.runAndWait() 

## have to set random seed, otherwise the text_input elements will be a mess on if-else conditions

#seed_no = random.randint(0,9) ## cannot be a random number everytime the page reloads
# better fix it for a certain time duration e.g. a day/ a particular hour
seed_no = datetime.now().hour

random.seed(seed_no)


audio_on = st.sidebar.selectbox("Speech recoginition mode",('Start','Stop'))

if audio_on == 'Start':


    st.header("Audio Bot")
    st.text("QnA")
    st.code("Please keep your answer within 5 seconds and allow Google 5 seconds to recognize your voice.")
    count=1
    for i in qna:

        st.write("Q"+str(count)+". "+i)
        tts(i)
        st.write("> Are you ready? Speak your answer after 1 second")
        #tts("Are you ready? Speak your answer after 1 second")
        #time.sleep(2)
        #count=rec(count)
        print(count)
        # st.write("I see! you like "+liked_ingredients)
        # tts("I see! you like "+liked_ingredients)
    
    st.write("Thank you for your response")

    tts("Thank you for your response")



