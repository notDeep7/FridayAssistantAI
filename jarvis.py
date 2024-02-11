import pyttsx3
import requests
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


    
def news():
    main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=4216d08a7101416aa1afd709f9e37d87'
    
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first", "second", 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'nineth', 'tenth']
    for ar in articles:
        head.append(ar["title"])
        
    for i in range(len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")
    
if __name__ == '__main__':
    wish()
    query = takecommand().lower()
    if "give news" in query:
        news()