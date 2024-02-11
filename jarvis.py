import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

#Speak Function for Friday Assistant
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#Speech Recognizer Function for Friday Assistant
    
def takecommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1 , phrase_time_limit=5)

    try:
        print("Recognizing...")
        query  =r.recognize_google(audio , language = 'en-in')
        print(f"user said:{query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query

if __name__ == '__main__':
    takecommand()
    speak("Good Morning Sir, the code is working!")
    