import pyttsx3
import speech_recognition as sr
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

#converting text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#converting voice to text
    
def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5 , phrase_time_limit=5)

    try:
        print("Recognizing...")
        query  =r.recognize_google(audio , language = 'en-in')
        print(f"user said:{query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query

#wish function

def wish():
    hour =  int(datetime.datetime.now().hour)
    # print(hour)
    
    if hour >= 0 and hour <=12:
        speak("Good Morning Sir")
    elif hour >12 and hour <=15:
        speak("Good Afternoon Sir")
    elif hour >15 and hour<=24:
        speak("Good Night Sir")

if __name__ == '__main__':
    wish()
    takecommand()
    speak("Good Morning Sir, the code is working!")
    