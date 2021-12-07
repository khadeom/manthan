#Speech to Text
import speech_recognition as sr
import scipy
import soundfile as sf

cnt=0
def speech_to_text(audio,rate,language="en",cnt=0):
  r = sr.Recognizer()
  wav_bytes = io.BytesIO()
  scipy.io.wavfile.write(wav_bytes, rate,audio)
  name="ans"+str(cnt)+".wav"
  sf.write(name, audio, 48000)

  with sr.AudioFile(wav_bytes) as source:
      audio = r.listen(source)
      # length=audio.size
      # audio = r.record(source,duration=10)
      #audio = r.listen(source, phrase_time_limit=5)
      
      try:
          text = r.recognize_google(audio)   #,language=)

          print("You said : {}".format(text))
          with open ("ans.txt","a+") as f:
            f.write("\nAns. ")
            f.write(text)

      except:
          print("Sorry could not recognize what you said")
      cnt+=1
          