from tkinter import *
import pyttsx3
from time import strftime
from PIL import ImageTk, Image
import webbrowser
import requests, json

ws = Tk()
width, height = ws.winfo_screenwidth(), ws.winfo_screenheight()
ws.geometry('%dx%d+0+0' % (width,height))
ws.title("Your Home Quarantine Guide")
ws['bg'] = '#5d8a82'

f = ("Times bold", 14)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def prevPage():
    ws.destroy()
    import page3

def time():
    string=strftime('%H:%M %p')
    timelabel.config(text=string)
    timelabel.after(1000,time)

def instruct():
    speak("Kindly look the time table carefully, I will remind you each and everything according to the time,  till then you can do you work")

button8=Button(
    ws,
    text="Click on me!",
    font=("Helvetica 30 bold"),
    bg="orange",
    relief=SUNKEN,
    borderwidth=5,
    command=instruct
).pack(pady=10)

def hq():
    webbrowser.open("https://youtu.be/qIX0-Sj8iIo")

def diet():
    webbrowser.open("https://youtu.be/z5UScMQUO6Q")

def yoga():
    webbrowser.open("https://youtu.be/M5et4-mqhvc")

def kaadhaa():
    webbrowser.open("https://youtu.be/c_wtziLCf_0")


image2 = Image.open('images/schedule.png')
image2 = image2.resize((600,550), Image.ANTIALIAS)
my_img2 = ImageTk.PhotoImage(image2)

ll=Label(
    ws,image=my_img2
).pack(side=LEFT,anchor="nw")

def out():
    ws.destroy()
    import instructor

insframe=Frame(ws,width=700,height=400, highlightcolor="white",highlightbackground="green", highlightthickness=10)
l=Label(insframe,text="SOME IMPORTANT THINGS!",font="Helvetica 40 bold",bg="yellow").pack(fill=X)
b1=Button(insframe,text="Click to know briefly about home quarantine",font=f,relief=SUNKEN,borderwidth=5,command=hq).pack(expand=TRUE, side=TOP,fill=X)
b2=Button(insframe,text="Click to know about healthy diet during quarantine",font=f,relief=SUNKEN,borderwidth=5,command=diet).pack(expand=TRUE, side=TOP,fill=X)
b3=Button(insframe,text="Click to know about Yoga and Pranayama during Quarantine",font=f,relief=SUNKEN,borderwidth=5,command=yoga).pack(expand=TRUE, side=TOP,fill=X)
b3=Button(insframe,text="Click to know how to make Kaadhaa",font=f,relief=SUNKEN,borderwidth=5,command=kaadhaa).pack(expand=TRUE, side=TOP,fill=X)
timelabel=Label(insframe,font=("ds-digital",40),background="black",foreground="cyan")
timelabel.pack(anchor="se",side=LEFT,ipady=50,ipadx=65)
b4=Button(insframe,text="Start Your Day Now!",font="Helvetica 30 bold",relief=SUNKEN,borderwidth=5,command=out,bg="light green").pack(side=LEFT,ipady=35)
insframe.pack(side=RIGHT,padx=30,anchor="nw",pady=50)


time()
button2=Button(
    ws,
    text="Prev Page",
    font=f,
    command=prevPage,relief=SUNKEN,borderwidth=5
).pack(side=BOTTOM,pady=50)

ws.mainloop()