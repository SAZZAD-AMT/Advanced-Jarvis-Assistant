from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore , QtWidgets , QtGui
from PyQt5.QtGui import QMovie
from PyQt5.uic import loadUiType
import sys
import pyttsx3
from SpeedTestUi import Ui_SpeedTest

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

def run_uit():

    Speak("I Am Checking Speed Sir , Wait For A While .")

    import speedtest

    speed = speedtest.Speedtest()

    upload = speed.upload()

    correct_Up = int(int(upload)/800000)

    download = speed.download()

    correct_down = int(int(download)/800000)

    Speak(f"Downloading Speed Is {correct_down} M B Per Second .")
    Speak(f"Uploading Speed Is {correct_Up} M B Per Second .")

    exit()

class MainThread(QThread):

    def __init__(self):

        super(MainThread,self).__init__()

    def run(self):
        run_uit()

StartExe = MainThread()

class StartExecution(QMainWindow):

    def __init__(self):

        super().__init__()

        self.ui = Ui_SpeedTest()

        self.ui.setupUi(self)

        self.ui.label = QMovie("E:\\YouTube Channel\\YouTube - Jarvis\\How To Make Jarvis In Python\\DataBase\\Gui Materials\\speedTest.gif")

        self.ui.gif.setMovie(self.ui.label)

        self.ui.label.start()

        StartExe.start()

App = QApplication(sys.argv)
speedtest = StartExecution()
speedtest.show()
exit(App.exec_())
