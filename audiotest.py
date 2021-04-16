import speech_recognition as sr
# This program allows you to turn speech to text (with slight delay)
# The second part then shows you the voices available on your system

import pyttsx3 

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Talk")
    audio_text = r.listen(source)   
    try:
        print(r.recognize_google(audio_text))
    except:
         print("Speak up please")


  
# initialisation 
engine = pyttsx3.init()
engine.setProperty("rate", 130)
voices = engine.getProperty("voices")
num=0
#engine.setProperty("voice", voices[0].id)
for i in voices:
    print(i)
    engine.setProperty("voice", voices[num].id)
    engine.say("This is voice "+str(num+1)) 
    engine.runAndWait()
    num+=1

# testing 
engine.say("this is the default voice") 
engine.runAndWait()
