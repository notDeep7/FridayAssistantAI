import pyttsx3
import requests
import speech_recognition as sr
import datetime
import os
import cv2
import random
import wikipedia
import webbrowser
import pywhatkit as pwt
from youtubesearchpython import VideosSearch
from requests import get
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


    
def news():
    main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=4216d08a7101416aa1afd709f9e37d87'
    
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first", "second", 'third']
    for ar in articles:
        head.append(ar["title"])
        
    for i in range(len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")
    
if __name__ == '__main__':
    wish()
    # speak("Good Morning Sir, the code is working!")
    while True:
        query = takecommand().lower()
#logic building for tasks
        
        if "open notepad" in query:
            npath = "C:\\Program Files\WindowsApps\\Microsoft.WindowsNotepad_11.2312.18.0_x64__8wekyb3d8bbwe\\Notepad\\Notepad.exe"
            os.startfile(npath)
        
        if "open spotify" in query:
            npath = "C:\\Users\\dashi\\AppData\\Local\\Microsoft\WindowsApps\\Spotify.exe"
            os.startfile(npath)
        
        if "please stop" in query:
            break

#play the music 

        if "play music" in query:
            music_dir = "D:\\music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif "shuffle music" in query:
            music_dir = "D:\\music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir,rd))

#show your ip address
            
        elif "show me ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP Address is {ip}")

        elif "give news" in query:
            news()

#search anything on wikipedia
            
        elif "wikipedia" in query:
            speak("Searching in wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences = 1)
            speak("according to wikipedia")
            speak(results)
        
#Play videos on youtube
            
        elif "play song on youtube" in query:
            # webbrowser.open("www.youtube.com")
            speak("What should i search sir?")
            cm = takecommand().lower()
            # webbrowser.open(f"{cm}")
            pwt.playonyt(f"{cm}")
