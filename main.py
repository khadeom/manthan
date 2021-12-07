from questions.py import qna
from text_to_voice.py import 






for i in range(len(qna[:5])):

  pause,count=text_to_voice(qna[i],count=i)

  time.sleep(pause)
  audio, rate = get_audio()
  speech_to_text(audio,rate,cnt=i)
  # clear()
with open ("ans.txt","a+") as f:
            f.write("====================================== ")