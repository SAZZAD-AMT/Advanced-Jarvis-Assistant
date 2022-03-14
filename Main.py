from types import coroutine
import pyttsx3
import speech_recognition as sr
from Features import GoogleSearch
from win10toast import ToastNotifier

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

def TaskExe():

    while True:

        query = TakeCommand()

        if 'google search' in query:
            GoogleSearch(query)
        
        elif 'youtube search' in query:
            Query = query.replace("jarvis","")
            query = Query.replace("youtube search","")
            from Features import YouTubeSearch
            YouTubeSearch(query)

        elif 'set alarm' in query:
            from Features import Alarm
            Alarm(query)

        elif 'download' in query:
            from Features import DownloadYouTube
            DownloadYouTube()
            
        elif 'speed test' in query:
            from Features import SpeedTest
            SpeedTest()

        elif 'whatsapp message' in query:

            name = query.replace("whatsapp message","")
            name = name.replace("send ","")
            name = name.replace("to ","")
            Name = str(name)
            Speak(f"Whats The Message For {Name}")
            MSG = TakeCommand()
            from Automations import WhatsappMsg
            WhatsappMsg(Name,MSG)

        elif 'call' in query:
            from Automations import WhatsappCall
            name = query.replace("call ","")
            name = name.replace("jarvis ","")
            Name = str(name)
            WhatsappCall(Name)

        elif 'show chat' in query:
            Speak("With Whom ?")
            name = TakeCommand()
            from Automations import WhatsappChat
            WhatsappChat(name)

        elif 'space news' in query:


            Speak("Tell Me The Date For News Extracting Process .")

            Date = TakeCommand()

            from Features import DateConverter

            Value = DateConverter(Date)

            from Nasa import NasaNews

            NasaNews(Value)

        elif 'about' in query:
            from Nasa import Summary
            query = query.replace("jarvis ","")
            query = query.replace("about ","")
            Summary(query)

        elif 'mars images' in query:

            from Nasa import MarsImage

            MarsImage()

        elif 'track iss' in query:

            from Nasa import IssTracker

            IssTracker()

        elif 'near earth' in query:
            from Nasa import Astro
            from Features import DateConverter
            Speak("Tell Me The Starting Date .")
            start = TakeCommand()
            start_date = DateConverter(TakeCommand)
            Speak("And Tell Me The End Date .")
            end = TakeCommand()
            end_date = DateConverter(end)
            Astro(start_date,end_date=end_date)

        elif 'my location' in query:

            from Features import My_Location

            My_Location()

        elif 'where is' in query:

            from Automations import GoogleMaps
            Place = query.replace("where is ","")
            Place = Place.replace("jarvis" , "")
            GoogleMaps(Place)

        elif 'online' in query:

            from Automations import OnlinClass

            Speak("Tell Me The Name Of The Class .")

            Class = TakeCommand()

            OnlinClass(Class)

        elif 'write a note' in query:

            from Automations import Notepad

            Notepad()

        elif 'dismiss' in query:

            from Automations import CloseNotepad

            CloseNotepad()

        elif 'time table' in query:

            from Automations import TimeTable

            TimeTable()

        elif 'activate the bulb' in query:

            from DataBase.HomeAuto.SmartBulb import Activate

            Activate()

            Speak("Should I Start Or Close The Bulb ?")

            step = TakeCommand()

            if 'close' in step:

                from DataBase.HomeAuto.SmartBulb import CloseLight

                CloseLight()

            elif 'start' in step:

                from DataBase.HomeAuto.SmartBulb import StartLight

                StartLight()

        elif 'corona cases' in query:

            from Features import CoronaVirus

            Speak("Which Country's Information ?")

            cccc = TakeCommand()

            CoronaVirus(cccc)

        else:

            from DataBase.ChatBot.ChatBot import ChatterBot

            reply = ChatterBot(query)

            Speak(reply)

            if 'bye' in query:

                break

            elif 'exit' in query:

                break

            elif 'go' in query:

                break

TaskExe()
