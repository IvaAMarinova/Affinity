import pyttsx3  
import speech_recognition as sr

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def get_voices(voice):
    voices = engine.getProperty('voices')
    if voice == 1:
        engine.setProperty('voice', voices[1].id)

        
get_voices(1)


speak("Strangers get born, strangers get buried\
Trends change, rumors fly through new skies\
But I'm right where you left me\
Matches burn after the other\
Pages turn and stick to each other\
Wages earned and lessons learned\
But I, I'm right where you left me\
Help, I'm still at the restaurant\
Still sitting in a corner I haunt\
Cross-legged in the dim light\
They say, What a sad sight\
I, I swear you could hear a hair pin drop\
Right when I felt the moment stop\
Glass shattered on the white cloth\
Everybody moved on\
I, I stayed there\
Dust collected on my pinned-up hair\
They expected me to find somewhere\
Some perspective, but I sat and stared\
Right where you left me\
You left me no, oh, you left me no\
You left me no choice but to stay here forever\
You left me, you left me no, oh, you left me no\
You left me no choice but to stay here forever\
Did you ever hear about the girl who got frozen?\
Time went on for everybody else, she won't know it\
She's still 23 inside her fantasy\
How it was supposed to be\
Did you hear about the girl who lives in delusion?\
Break-ups happen every day, you don't have to lose it\
She's still 23 inside her fantasy\
And you're sitting in front of me\
At the restaurant, when I was still the one you want\
Cross-legged in the dim light, everything was just right\
I, I could feel the mascara run\
You told me that you met someone\
Glass shattered on the white cloth\
Everybody moved on\
Help, I'm still at the restaurant\
Still sitting in a corner I haunt\
Cross-legged in the dim light\
They say, What a sad sight\
I, I stayed there\
Dust collected on my pinned-up hair\
I'm sure that you got a wife out there\
Kids and Christmas, but I'm unaware\
'Cause I'm right where\
I cause no harm, mind my business\
If our love died young, I can't bear witness\
And it's been so long\
But if you ever think you got it wrong\
I'm right where you left me\
You left me no, oh, you left me no\
You left me no choice but to stay here forever\
You left me\
You left me no, oh, you left me no\
You left me no choice but to stay here forever")