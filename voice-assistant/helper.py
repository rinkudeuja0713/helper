import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import pyaudio
import os
from PyDictionary import PyDictionary

dictionary = PyDictionary()




engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def take_cmd():
    rc = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        rc.pause_threshold = 1
        audio = rc.listen(source)
    try:
        print("Recognizing....")
        query = rc.recognize_google(audio, language='en-in')
        print("You said :" + query + "\n")
    except Exception as e:
        print(e)
        speak("Sorry, i could not understand")
        return "None"
    return query

if __name__ == '__main__':

    speak("Hi, I am helper. Here to assist you")
    speak("How can I help you")
    while True:
        query = take_cmd().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia ...")
            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
        
        elif 'meaning' in query:
            speak("searching Dictionary....")
            search_query = query.split("meaning of",1)[-1].strip()
            speak(f"Searching for the meaning of {search_query}")
            definition = dictionary.meaning(search_query)
            print(f"definition of {search_query} : {definition}")
            speak(f"definition of {search_query} : {definition}")
       

        elif 'are you' in query:
            speak("I am Helper. Made by Rinku Deuja to assist in simple tasks such as opening certain websites, searching youtube,wikipedia,et cetera")
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
   
        elif 'can you search' and 'on youtube' in query:
            search_query = query.split("can you search", 1)[-1].strip()
            search_query1 = search_query.split("on youtube", 1)[0].strip()
            speak(f"Searching for {search_query1} on youtube ")
            search_url = f"https://www.youtube.com/results?search_query={search_query1}"
            webbrowser.open(search_url)

        elif 'open chatgpt' in query:
            speak("opening chatgpt")
            webbrowser.open("https://chat.openai.com/")

            
        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")
        elif 'open github' in query:
            speak("opening github")
            webbrowser.open("github.com")
       
        elif 'open spotify' in query:
            speak("opening spotify")
            webbrowser.open("spotify.com")

        elif 'play music' in query:
            speak("opening music")
            webbrowser.open("spotify.com")
        elif 'local disk d' in query:
            speak("opening local disk D")
            webbrowser.open("D://")
        elif 'local disk c' in query:
            speak("opening local disk C")
            webbrowser.open("C://")
        elif 'local disk e' in query:
            speak("opening local disk E")
            webbrowser.open("E://")
        elif 'goodbye' in query:
            exit(0)
    
    
