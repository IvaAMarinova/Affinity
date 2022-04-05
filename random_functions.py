import pyttsx3  
import speech_recognition as sr
import datetime
import smtplib
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

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def get_voices(voice):
    voices = engine.getProperty('voices')
    if voice == 1:
        engine.setProperty('voice', voices[1].id)
        
def time():
    Time = datetime.datetime.now().strftime('%I:%M:%S')
    speak("The current time is:")
    speak(Time)

def introduction():
    speak("What am i? A great question!")
    print("What am i? A great question!")
    speak("I am a one of a kind personal assistant!")
    print("I am a one of a kind personal assistant!")
    speak("My job is to help you live your life as easy as possible, ")
    print("My job is to help you live your life as easy as possible, ")
    speak("while bringing in a grain of humor")
    print("while bringing in a grain of humor")
    speak("go piss girl")
    print("go piss girl")


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak("The current date is:")
    speak(day)
    speak(month)
    speak(year)

def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour <12:
        speak("Good morning!")
    elif hour >= 12 and hour <18: 
        speak("Good afternoon!")
    elif hour >= 18 and hour < 24:
        speak("Good evening!")
    else: 
        speak("Good night!")

def wish_me():
    greeting()
    time()
    date()
    speak("Affinity at your service. Is there something i can help you with?")

def take_ommand_CMD():
    query = input("Is there something i can help you with?\n")
    return query


def take_command_mic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try: 
        print("Recognizing...")
        query = r.recognize_google(audio, language='en')
        print(query)
    except Exception as e:
        print(e)
        speak("Can you repeat that?")
        print("Can you repeat that?...")
        return "None"
    return query


def search_google():
    speak('What should i search for?')
    search = take_command_mic()
    wb.open('https://www.google.com/search?q='+search)


def news():
    newsapi = NewsApiClient(api_key='7ed4eab6f966410188060a66982f2b3e')
    speak('What topic are you interested in today?')
    topic = take_command_mic()
    data = newsapi.get_top_headlines(q=topic,
                                    language='en',
                                    page_size=5)
    newsdata = data['articles']
    for x,y in enumerate(newsdata):
        print(f'{x}{y["description"]}')
        speak((f'{x}{y["description"]}'))

    speak("These were the most important news for now!")


def text_to_speech():
    text = clipboard.paste()
    print(text)
    speak(text)


#name_img = tt.time()
    #name_img = f'D:\\Github\\Screenshots\\{name_img}.png' #works for iva
    #img = pyautogui.screenshot(name_img)
    #img.show()


if __name__ == "__main__":
    get_voices(1)
    wish_me()
    #greeting()
    
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
            #speak("suzdadeno prez 1988 г., то има за цел да подготвя средни специалисти в областта на историята и философията. Първоначално директор е Златка Петрова, а заместник-директор е Стефан Чернаев. Директор на училището е д-р Анатол Френски.")

        elif 'search' in query:
            search_google()

        elif 'youtube' in query:
            #speak("What should i search for on YouTube?")
            #topic = take_command_mic()
            kit.playonyt("7 Rings song")
            print("Playing...")

        elif 'news' in query: #iva
            news()

        elif 'read' in query:
            text_to_speech()

        elif 'open editor' in query: #
            codepath = 'C:\\Users\\ivama\\.vscode'
            os.startfile(codepath)

        elif 'joke' in query: #
            joke = pyjokes.get_joke(language="en", category="all")
            print(joke)
            speak(joke)
            
        #elif 'screenshot' in query:
            #screenshot()
            #print("Screenshot taken")
    
        elif 'offline' in query:
            speak("Going offline")
            print("Going offline")
            quit()

        elif 'introduction' in query:
            introduction()

        elif 'legends' in query: #
            speak('Not gonna happen')
            print('Not gonna happen')


        else:
            speak("Can you repeat that?")
            print("Can you repeat that?")

       
        
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