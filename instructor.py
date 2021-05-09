from datetime import datetime
import time
from win10toast import ToastNotifier
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

toaster = ToastNotifier()


def isTimeCorrect(input):
    try:
        time.strptime(input, '%H:%M:%S')
        return True
    except ValueError:
        return print('time is wrong')

alarm1 = "23:15:00"
alarm2 = "23:15:30"
alarm3 = "23:16:00"
alarm4 = "23:16:30"
alarm5 = "23:17:00"
alarm6 = "23:17:30"
alarm7 = "23:18:00"
alarm8 = "23:18:30"
alarm9 = "23:19:00"
alarm10 = "23:19:30"
alarm11 = "23:20:00"
alarm12 = "23:20:30"
alarm13 = "23:21:00"
alarm14 = "23:21:30"
alarm15 = "23:22:00"
alarm16 = "23:22:30"
alarm17 = "23:23:00"

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
while (isTimeCorrect(alarm1)):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if current_time == alarm1:
        toaster.show_toast("Hello!","It's YOUR HOME QUARANTINE GUIDE", icon_path=None, duration=5, threaded=True)
        speak("It's 06:30 AM , you have to do Yoga and Pranayam for 30 minutes")
        break

while (isTimeCorrect(alarm2)):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if current_time == alarm2:
        toaster.show_toast("Hello!","It's YOUR HOME QUARANTINE GUIDE", icon_path=None, duration=5, threaded=True)
        speak("It's 07:00 AM ,  Take a glass of hot lemon water")
        break

while (isTimeCorrect(alarm3)):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if current_time == alarm3:
        toaster.show_toast("Hello!","It's YOUR HOME QUARANTINE GUIDE", icon_path=None, duration=5, threaded=True)
        speak("It's 08:00 AM ,   Please have a healthy breakfast")
        break

while (isTimeCorrect(alarm4)):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if current_time == alarm4:
        toaster.show_toast("Hello!","It's YOUR HOME QUARANTINE GUIDE", icon_path=None, duration=5, threaded=True)
        speak("It's 08:30 AM ,   Please take a glass of hot milk")
        break

while (isTimeCorrect(alarm5)):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if current_time == alarm5:
        toaster.show_toast("Hello!","It's YOUR HOME QUARANTINE GUIDE", icon_path=None, duration=5, threaded=True)
        speak("It's 09:00 AM ,   Please take steam for 10 minutes")
        break

while (isTimeCorrect(alarm6)):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if current_time == alarm6:
        toaster.show_toast("Hello!","It's YOUR HOME QUARANTINE GUIDE", icon_path=None, duration=5, threaded=True)
        speak("It's 09:30 AM ,   Please take 100 ML kaadhaa")
        break


while (isTimeCorrect(alarm7)):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if current_time == alarm7:
        toaster.show_toast("Hello!","It's YOUR HOME QUARANTINE GUIDE", icon_path=None, duration=5, threaded=True)
        speak("It's 11:00 AM ,   Please take 50 ML of hot tea")
        break


while (isTimeCorrect(alarm8)):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if current_time == alarm8:
        toaster.show_toast("Hello!","It's YOUR HOME QUARANTINE GUIDE", icon_path=None, duration=5, threaded=True)
        speak("It's 12:00 PM ,   Take a glass of hot lemon water")
        break


while (isTimeCorrect(alarm9)):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if current_time == alarm9:
        toaster.show_toast("Hello!","It's YOUR HOME QUARANTINE GUIDE", icon_path=None, duration=5, threaded=True)
        speak("It's 01:00 PM ,   Please have a healthy lunch")
        break


while (isTimeCorrect(alarm10)):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if current_time == alarm10:
        toaster.show_toast("Hello!","It's YOUR HOME QUARANTINE GUIDE", icon_path=None, duration=5, threaded=True)
        speak("It's 02:00 PM ,   Please take steam for 10 minutes")
        break



while (isTimeCorrect(alarm11)):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if current_time == alarm11:
        toaster.show_toast("Hello!","It's YOUR HOME QUARANTINE GUIDE", icon_path=None, duration=5, threaded=True)
        speak("It's 04:00 PM,   Please take some rest and don't forget to drink kaadhaa at 05:30 PM")
        break


while (isTimeCorrect(alarm12)):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if current_time == alarm12:
        toaster.show_toast("Hello!","It's YOUR HOME QUARANTINE GUIDE", icon_path=None, duration=5, threaded=True)
        speak("It's 06:00 PM,   Please do some Yoga")
        break


while (isTimeCorrect(alarm13)):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if current_time == alarm13:
        toaster.show_toast("Hello!","It's YOUR HOME QUARANTINE GUIDE", icon_path=None, duration=5, threaded=True)
        speak("It's 07:00 PM ,   Take a glass of hot lemon water")
        break



while (isTimeCorrect(alarm14)):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if current_time == alarm14:
        toaster.show_toast("Hello!","It's YOUR HOME QUARANTINE GUIDE", icon_path=None, duration=5, threaded=True)
        speak("It's 07:30 PM ,   Take a healthy dinner")
        break



while (isTimeCorrect(alarm15)):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if current_time == alarm15:
        toaster.show_toast("Hello!","It's YOUR HOME QUARANTINE GUIDE", icon_path=None, duration=5, threaded=True)
        speak("It's 09:00 PM ,   Please take steam for 10 minutes")
        break



while (isTimeCorrect(alarm16)):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if current_time == alarm16:
        toaster.show_toast("Hello!","It's YOUR HOME QUARANTINE GUIDE", icon_path=None, duration=5, threaded=True)
        speak("It's 09:30 PM ,   Please take 100 ML kaadhaa")
        break



while (isTimeCorrect(alarm17)):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if current_time == alarm17:
        toaster.show_toast("Hello!","It's YOUR HOME QUARANTINE GUIDE", icon_path=None, duration=5, threaded=True)
        speak("It's 10:30 PM ,   Please a glass of hot milk ,    and please sleep now,   Good Night Mate!")
        break