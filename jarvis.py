import time
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
import smtplib
import pyautogui as pag
from youtubesearchpython import VideosSearch
from requests import get
import openai
#INITIALIZING THE ENGINE
engine = pyttsx3.init('sapi5')
#INITIALIZING THE VOICES IN THE ENGINE
voices = engine.getProperty('voices')
#SETTING THE VOICES

engine.setProperty('voice', voices[1].id)

#FETCHING COOKIES OF BARD
openai.api_key = "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"

def chat_with_gpt(prompt):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages = [{"role":"user","content":prompt}]

    )
    return response.choices[0].message.content.strip()

#CONVERTING TEXT TO SPEECH (OUTPUT SPEECH)
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#CONVERTING VOICE TOM TEXT (INPUT COMMAND)
    #SPEECH RECOGNIZATION
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

#WISH FUNCTION

def wish():
    hour =  int(datetime.datetime.now().hour)
    # print(hour)
    
    if hour >= 0 and hour <=12:
        speak("Good Morning Sir")
    elif hour >12 and hour <=15:
        speak("Good Afternoon Sir")
    elif hour >15 and hour<=24:
        speak("Good Night Sir")


#EMAIL SENDER USING SMTP
        

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('sender_email','your_email_app_password')
    server.sendmail('sender_email',to,content)
    server.close()

#NEWS GENERATOR 
    
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

#MAIN LOBBY
    
if __name__ == '__main__':
    wish()
    # speak("Good Morning Sir, the code is working!")
    while True:
        query = takecommand().lower()

#LOGIC BUILDING FOR TASKS
        
        if "open notepad" in query:
            npath = "C:\\Program Files\WindowsApps\\Microsoft.WindowsNotepad_11.2312.18.0_x64__8wekyb3d8bbwe\\Notepad\\Notepad.exe"
            os.startfile(npath)
        if "close notepad" in query:
            os.system("taskkill /f /im notepad.exe")
#OPENING SPOTIFY      
        if "open spotify" in query:
            npath = "C:\\Users\\dashi\\AppData\\Local\\Microsoft\WindowsApps\\Spotify.exe"
            os.startfile(npath)
        if "close spotify" in query:
            os.system("taskkill /f /im Spotify.exe")
#STOPPING THE CODE       
        if "you can stop now" in query:
            speak('Thank you sir, and have a great day!')
            break

#PLAY THE MUSIC

        if "play music" in query:
            music_dir = "D:\\music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))

#SHUFFLE MUSIC USING RANDOM()  
            
        elif "shuffle music" in query:
            music_dir = "D:\\music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir,rd))

#SHOW YOUR IP ADDRESS
            
        elif "show me ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP Address is {ip}")

        elif "give news" in query:
            news()

#SEARCH ANYTHING ON WIKIPEDIA
            
        elif "wikipedia" in query:
            speak("Searching in wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences = 1)
            speak("according to wikipedia")
            speak(results)
        
#PLAY VIDEOS ON YOUTUBE
            
        elif "play song on youtube" in query:
            # webbrowser.open("www.youtube.com")
            speak("What should i search sir?")
            cm = takecommand().lower()
            # webbrowser.open(f"{cm}")
            pwt.playonyt(f"{cm}")

#SEARCH ANYTHING IN GOOGLE
            
        elif "search on google" in query:
            
            speak("What should i search sir?")
            cm = takecommand().lower()
            pwt.search(f"{cm}")

#SEND MESSAGE THROUGH WHATSAPP
            
        elif "send message" in query:
            speak("What message should i send?")
            cm = takecommand().lower()
            pwt.sendwhatmsg("+917908963371",f"{cm}",8,28)

#SEND EMAIL THROUGH SMTP 
            
        elif "send email" in query:
            try:
                speak("What should i say?")
                content = takecommand().lower()
                to = "receiver_email"
                sendEmail(to,content)
                speak("Email has been sent to the user")

            except Exception as e:
                print(e)
                speak("sorry sir,i am not able to send!")

#SHUTDOWN THE SYSTEM
        elif "shut down the system" in query:
            os.system("shutdown /s /t 5")

#RESTART THE SYSTEM
        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

#SLEEP THE SYSTEM
        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

#SWITCH THE WINDOW
        elif "switch the window" in query:
            pag.keyDown("alt")
            pag.press("tab")
            time.sleep(1)
            pag.keyUp("alt")
        
        else:
            response = chat_with_gpt(query)
            speak(response)
