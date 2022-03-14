from re import S
import pyttsx3
import speech_recognition as sr
import pyautogui 
import os
import keyboard
from time import sleep

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

def TakeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print(": Listening....")

        r.pause_threshold = 1

        audio = r.listen(source)


    try:

        print(": Recognizing...")

        query = r.recognize_google(audio,language='en-in')

        print(f": Your Command : {query}\n")

    except:
        return ""

    return query.lower()

def Activate():

    try:

        os.system('TASKKILL /F /im HD-Player.exe')

    except Exception as e:
        print(e)

    Speak("Activating The Home Automation Setup.")

    keyboard.press_and_release('windows + s')

    sleep(1)

    keyboard.write('blue')

    sleep(1)

    keyboard.press('enter')

    sleep(20)

    pyautogui.click(x=1157, y=81)
    
    sleep(5)

    pyautogui.click(x=553, y=148)

    sleep(3)

    Speak("Activated The Home Setup .")
    
def StartLight():

    Speak("Activating The Smart Bulb .")

    pyautogui.click(x=820, y=187)

    Speak("Activated.")

def CloseLight():

    Speak("Closing The Smart Bulb .")

    pyautogui.click(x=820, y=187)

    Speak("Closed.")

