import speech_recognition as sr
import webbrowser
import pyttsx3
from musiclibrary import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTS
import pygame
import os
from datetime import datetime
import time

recognizer = sr.Recognizer()
engine = pyttsx3.init() 
newsapi = "<c6a26a8e4c8849cc9b46cced65d13a6c>"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3') 

    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 
    
client = OpenAI(api_key="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")

def aiProcess(command):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud."},
            {"role": "user", "content": command}
        ]
    )
    return completion.choices[0].message.content

def set_alarm(time_str):
    time_str = time_str.replace(".", "").strip()
    alarm_time = None
    for fmt in ("%I:%M %p", "%I %p"):
        try:
            alarm_time = datetime.strptime(time_str, fmt).time()
            break
        except ValueError:
            continue
    if alarm_time is None:
        speak("Sorry, I couldn't understand the time format.")
        return

    speak(f"Alarm set for {time_str}")
    while True:
        now = datetime.now().time()
        if now.hour == alarm_time.hour and now.minute == alarm_time.minute:
            speak("Time to wake up!")
            break
        time.sleep(10)



def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open pinterest" in c.lower():
        webbrowser.open("https://pinterest.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])

    elif "set alarm for" in c.lower():
        try:
            # Find the index after the phrase "set alarm for"
            idx = c.lower().find("set alarm for") + len("set alarm for")
            # Extract everything after that index and strip whitespace
            time_str = c[idx:].strip()
            print(f"DEBUG: Alarm time extracted: '{time_str}'")
            set_alarm(time_str.upper())
        except Exception as e:
            print(f"Alarm error: {e}")
            speak("Sorry, I couldn't set the alarm. Please try again.")

    else:
        # Let OpenAI handle the request
        output = aiProcess(c)
        speak(output) 

if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
            # Listen for the wake word "Jarvis"
            # obtain audio from the microphone
        r = sr.Recognizer()
            
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                    print("Listening...")
                    audio = r.listen(source, timeout=7, phrase_time_limit=6)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya")
                    # Listen for command
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))


