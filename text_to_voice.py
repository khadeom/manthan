from gtts import gTTS
from playsound import  playsound
from IPython.display import Audio
from IPython.display import display
import time
import mutagen
from mutagen.mp3 import MP3


def text_to_voice(mytext,language="en",count=0):

  # mytext="Hello ho ja re did it work"
  # language='hi'
  with open ("ans.txt","a+") as f:
            f.write("\nQ. ")
            f.write(mytext)
  myobj=gTTS(text=mytext,lang=language)
  name="que"+str(count)+".mp3"
  myobj.save(name)   #saving audio
  un=Audio(name,autoplay=True)
  display(un)
  v=MP3("/content/"+name)
  count+=1
  return (int(v.info.length)+1), count
  