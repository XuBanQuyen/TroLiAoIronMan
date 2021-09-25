import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os
ironman = pyttsx3.init()
voice = ironman.getProperty('voices')
ironman.setProperty('voice',voice[1].id)

def speak(audio):
    print("XuBanQuyen:"+(audio))
    ironman.say(audio)
    ironman.runAndWait()
def time():
    Time = datetime.datetime.now().strftime('%I,%M.%p')
    speak(Time)

def welcome():
    hour = datetime.datetime.now().hour
    if hour >=6 and hour <12:
        speak("Good Morning,sir")
    elif hour >=12 and hour <18:
        speak("Good Afternoon,sir")
    elif hour >=18 and hour <24:
        speak("Good Night,sir")
    speak('How can I help you')
def command():
    c = sr.Recognizer()
    with sr.Microphone() as source:
        c.pause_threshold=2
        audio=c.listen(source)
    try:
        query=c.recognize_google(audio,language='en')
        print("Tony Leo :"+query)
    except sr.UnknownValueError:
        print("Please repeat or tying the command")
        query=str(input("Your order is: "))
    return query

if __name__ == '__main__':
    welcome()
    while True:
        query=command().lower()
        if "google" in query:
            speak("What should I search Boss?")
            search=command().lower()
            url=f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on google')
        if "youtube" in query:
            speak("What should I search Boss?")
            search=command().lower()
            url=f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f'Here is your {search} on youtube')
        elif "open video":
            meme = r"D:\đi bar cũng nhớ về q....mp4"
            os.startfile(meme)
        elif "time" in query:
            time()
        elif "quick" in query:
            speak("Ironman is quitting sir.Goodbye Boos")
            quit()
