'''  modules required

1. text to speech converter -- pyttsx3 
2. speech recognition voice to text converter -- speech_recognition
3. web searching -- webbrowser
4. for getting date and time -- datetime
5. for jokes -- pyjokes 

'''
import pyttsx3
import speech_recognition
import webbrowser
import pyjokes
import datetime

print("_______   Welcome to Your_Voice_Assistant  ______",end="\n\n")

def sptext():
    recognizer= speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("I am Listening .....",end="\n\n")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("I am recognizing...",end="\n\n")
            data=recognizer.recognize_google(audio)
            print("You said --> ",data)
        except speech_recognition.UnknownValueError:
            print("Sorry i was'nt able to understand please try again! ")


def speechtx():
    engine= pyttsx3.init()
    voices= engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    rate=engine


sptext()