# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 16:25:38 2019

@author: Riad
"""

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import numpy as np
from PyLyrics import *
from PyDictionary import PyDictionary

dictionary=PyDictionary()
try: 
    from googlesearch import search 
except ImportError:  
    print("No module named 'google' found") 
engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def WishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Sir")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
        
    speak("How can i help you?")
def wait():
    signal=command()
    while(signal !="Hello"):
        wait()

def command():
    r= sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold= 1
        audio= r.listen(source)
    try:
        print('Recognising..')
        query=r.recognize_google(audio)
        print("You said: ",query)
    except Exception as e:
        print("Sorry i can't understand..Say Again..")
        return "none"
    return query

if __name__=="__main__":
    speak("Hello.. I am jack..")
    default=["Could not understand","Sorry sir Say again..","All i could not undersatand.. i am a beginner.. Say again sir.."]
    WishMe()
    while True:
        query=command().lower()
        
        if 'wikipedia' in query:
            speak("searching wikipedia..")
            query= query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            print(results)
            speak("According to wikipedia..")
            speak(results)
            speak("Anything Sir?")
            counter_wiki=+1
        elif 'meaning' in query:
            query=query.replace("meaning","")
            print (dictionary.meaning(query))
            speak("Here is sir")
            counter_meaning=+1
        elif 'who are you' in query or 'your name' in query:
            speak("I am jack 1.0")
            counter_jack=+1
        elif 'how are you' in query:
            speak("I am always fine....")
            counter_jack=+1
        elif 'hello' in query or 'what\'s up' in query :
            speak("Hi Sir")
            counter_hello=+1
        elif 'about you' in query:
            with open("Jack_info.txt",'r') as rf:
                rf_contents=rf.read()
            speak(rf_contents)
            counter_jack=+1
        elif 'browse' in query:
            index=query.find('browse')
            index=index+len('browse')
            query=query.replace(query[0:index],"")
            webbrowser.open(query+".com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'who created you' in query or 'who is your creator' in query:
            speak("Riad Ahmed is my creator..")
            speak("Anything else Sir?")
        elif 'riyadh ahmed' in query:
            speak("Riad Ahmed is my creator")
            speak("Anything else?")
        elif 'lyrics' in query:
            speak("What is the song?")
            song=command()
            print(song)
            speak("Who is the singer?")
            singer=command()
            print(singer)
            print(PyLyrics.getLyrics(singer,song))
            speak("Done")
            speak("Anything sir?")
            #Print the lyrics directly
        elif 'do you know' in query:
            query= query.replace("do you know","")
            speak("Yes i know....")
            
            results=wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)
        elif 'favourite photo' in query:
            photo_dir="E:\\temp\\Purno\\New folder"
            photo=os.listdir(photo_dir)
            os.startfile(os.path.join(photo_dir,photo[np.random.randint(2)]))
            speak("I just opened your favourite photo.. Check it")
           # os.open(photo_dir)
        elif 'say about' in query:
            
            speak("searching ..")
            index=query.find('say about')
            index=index+len('say about')
            query=query.replace(query[0:index],"")
            
            results=wikipedia.summary(query,sentences=2)
            print(results)
            
            speak("According to wikipedia..")
            speak(results)
        elif 'search' in query:
            query= query.replace("search","")
            url="https://google.com/search?q=%s" % query
            webbrowser.open(url, new=0, autoraise=True)
            speak("I searched "+ query)
        elif 'play music' in query:
            music_dir='F:\\Others\\Mp3 songs\\Sounds\\Music'
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[np.random.randint(100)]))
        elif 'save ' in query:
            speak("Ok Sir.. I am ready..")
            speak("What type of information sir?")
            info_type=command()
            if 'task' in info_type:
                speak("I am recording Sir.. Stay saying..")
                task=command()
                with open("task.txt",'w') as wf:
                    wf.write(task)
                    
                speak("Done")
        elif 'saved information' in query:
            speak("Ok Sir..")
            speak("You said..")
            with open("task.txt",'r') as rf:
                rf_cont=rf.read()
                rf_cont=rf_cont.replace("i ","you")    
                speak(rf_cont)
            
        elif 'quit' in query or 'no' in query or 'stop' in query:
            
            with open("termination_statement.txt",'r') as rf:
                rf_contents=rf.read()
            speak(rf_contents)
            break
        else:
            #speak("I could not understand.. Say again sir..")
            speak(default[np.random.randint(3)])
        
    