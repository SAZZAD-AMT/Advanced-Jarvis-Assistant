from datetime import datetime
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[2].id)

def Speak(audio):
    print(" ")
    print(f": {audio}")
    engine.say(audio)
    engine.runAndWait()
    print(" ")

FiveTo6 = '''
In This Time , 
You Have To Get Up & Listen Somethintg Positive .
5:00 Am To 6:00 Am 
Thanks.
'''

SixTo9 = '''
In This Time , 
You Have To Study .
6:00 Am To 9:00 Am .
Thanks .
'''

NineTo12 = '''
In This Time ,
You Have A Make A Video & Have To Upload It On YouTube .
9:00 Am To 12:00 Pm .
Thanks .
'''

TwelveTo15 = '''
In This Time ,
You Have To Gain Some Knowledge From The Internet OR From Your Books .
12:00 Pm To 3:00 Pm .
Thanks .
'''

FifteenTo21 = '''
In This Time ,
You Have To Code .
3:00 Pm To 9:00 Pm .
Thanks .
'''

TwentyOneTo22 = '''
In This Time ,
You Have To Sleep .
9:00 Pm To 10:00 Pm .
Thanks .
'''

def Time():

    hour = int(datetime.now().strftime("%H"))

    if hour>=5 and hour<6:
        Speak(FiveTo6)
        return FiveTo6
        
    elif hour>=6 and hour<9:
        Speak(SixTo9)
        return SixTo9

    elif hour>=9 and hour<12:
        Speak(NineTo12)
        return NineTo12

    elif hour>=12 and hour<15:
        Speak(TwelveTo15)
        return TwelveTo15

    elif hour>=15 and hour<21:
        Speak(FifteenTo21)
        return FifteenTo21

    elif hour>=21 and hour<22:
        Speak(TwentyOneTo22)
        return TwentyOneTo22
        
    else:
        Speak("In This Time , You Have To Sleep ")

        return '''In This Time , You Have To Sleep .'''
