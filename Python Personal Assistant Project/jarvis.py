import os
import webbrowser

import pyttsx3
from datetime import datetime
import speech_recognition as sr
import wikipedia
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)





def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.now().hour)
    if(hour >= 0 and hour < 12):
        speak("Good Morning..!")
    elif(hour >=12 and hour < 16):
        speak("Good After Noon..!")
    else:
        speak("Good Evening..!")

    speak("Hi I am jarvis sir . What can I do for you ..!")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=2)
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print("User said :", query)

    except Exception as e:
        print(e)
        print('Say that again plz...')
        return None
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smntp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('123015128@sastra.ac.in','nani2107')
    server.sendemail('123015128@sastra.ac.in',to ,content)
    server.close()

if __name__ == "__main__":
    try:
        wishMe()
        while True:
            query = takeCommand()
            if 'Wikipedia' in query:
                speak("Searching Wikipedia...")
                query = query.replace('Wikipedia', '')
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia ")
                print(results)
                speak(results)
            if 'open Chrome' in query:
                webbrowser.open_new_tab("google.com")
            if 'open Youtube' in query:
                webbrowser.open_new_tab("youtube.com")
            elif 'the time' in query:
                strTime = datetime.now().strftime("%H:%M:%S")
                speak(strTime)
            elif 'play music' in query:
                music_dir = 'E:\MP3\ABCD'
                song = os.listdir(music_dir)
                print(song)
                os.startfile(os.path.join(music_dir, song[0]))
            elif 'email to Nani'in query:
                try:
                    speak('What should i send :')
                    content = takeCommand()
                    to ='srinivasnani2107@gmail.com'
                    sendEmail(to,content)
                    speak("Email has sent !")
                except Exception as e:
                    print(e)
                    speak("Sorry sir. I was unable to send an Email")
            elif 'quit' in query:
                exit()

    except Exception as e:
        print(e)

