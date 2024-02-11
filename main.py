import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


if __name__ == '__main__':
    speak("Good Morning Sir, the code is working!")
    