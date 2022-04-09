import pyttsx3  
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser as wb
import pywhatkit  as kit
from newsapi import NewsApiClient
import clipboard
import os
import pyjokes
import pyautogui
import time as tt
#import spotipy
import json
#import requests
#import wolframalpha 
from dotenv import load_dotenv
load_dotenv() 

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    return audio


def get_voices(voice):
    voices = engine.getProperty('voices')
    if voice == 1:
        engine.setProperty('voice', voices[1].id)
        
def time():
    Time = datetime.datetime.now().strftime('%I:%M:%S')
    speak("The current time is:")
    speak(Time)

def introduction():
    print(speak("What am i? A great question!"))
    print(speak("I am a one of a kind personal assistant!"))
    print(speak("My job is to help you live your life as easy as possible, "))
    print(speak("while bringing in a grain of humor"))

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    print(speak("The current date is: "), speak(day), '.', speak(month), '.', speak(year))


def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        print(speak("Good morning!"))
    elif hour >= 12 and hour < 18: 
        print(speak("Good afternoon!"))
    elif hour >= 18 and hour < 24:
        print(speak("Good evening!"))
    else: 
        print(speak("Good night!"))


def wish_me():
    greeting()
    time()
    date()
    print(speak("Affinity at your service. Is there something i can help you with?"))


def take_command_CMD():
    query = input("Is there something i can help you with?\n")
    return query


def take_command_mic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print(speak("Listening..."))
        r.pause_threshold = 1
        audio = r.listen(source)
    try: 
        print(speak("Recognizing..."))
        query = r.recognize_google(audio, language='en')
        print(query)
    except Exception as e:
        print(e)
        print(speak("Can you repeat that?"))
        return "None"
    return query


def search_google():
    speak('What should i search for?')
    search = take_command_mic()
    wb.open('https://www.google.com/search?q='+search)


def news():
    newsapi = NewsApiClient(api_key=os.getenv('API_KEY'))
    print(speak('What topic are you interested in today?'))
    topic = take_command_mic()
    data = newsapi.get_top_headlines(q=topic,
                                    language='en',
                                    page_size=5)
    newsdata = data['articles']
    for x,y in enumerate(newsdata):
        print(speak((f'{x}{y["description"]}')))

    print(speak("These are the most important news for now!"))


def text_to_speech():
    text = clipboard.paste()
    print(speak(text))


if __name__ == "__main__":
    get_voices(1)
    wish_me()  

    while True:
        query = take_command_mic().lower()  

        if 'time' in query :
            time()

        elif 'date' in query:
            date()

        elif 'wikipedia' in query:
            speak('Searching on Wikipedia...')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 2)
            print(result)
            speak(result)

        elif 'search' in query:
            search_google()

        elif 'youtube' in query:
            speak("What should i search for on YouTube?")
            topic = take_command_mic()
            kit.playonyt(topic)
            print(speak("Playing..."))

        elif 'news' in query: 
            news()

        elif 'read' in query:
            text_to_speech()

        elif 'open editor' in query:
            codepath = 'C:\\Users\\' + os.getenv('USERNAME') + '\\.vscode'
            os.startfile(codepath)

        elif 'joke' in query:
            joke = pyjokes.get_joke(language="en", category="all")
            print(joke)
            speak(joke)
            
    
        elif 'offline' in query:
            quit()

        elif 'introduction' in query:
            introduction()

        #just a League of Legends joke
        elif 'legends' in query: 
            print(speak('Not gonna happen'))

        else:
            print(speak("Sorry, I could not hear you."))
            print("Sorry, I could not hear you.")

       
        
        """elif 'remember':
            speak("What should i remember?")
            data = take_command_mic()
            speak("remembered" +data)
            remember = open('remembered_data.txt', 'w')
            remember.write(data)
            remember.close()
        elif 'tell them what i told you':
            remembered = open('remembered_data.txt', 'r')
            speak("You told me that" +remembered.read())"""