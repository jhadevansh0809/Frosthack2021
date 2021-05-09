from tkinter import *
import pyttsx3
import datetime
import pickle

file = open('model.pkl', 'rb')
clf = pickle.load(file)
file.close()

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


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Superwoman and I am your guide for this home quarantine,I promise you will be alright!,Please fill the entries below")

def nextPage():
    ws.destroy()
    import page4


def prevPage():
    ws.destroy()
    import page2


button4=Button(
    ws,
    text="Click on me!",
    font=("Helvetica 30 bold"),
    bg="orange",
    relief=SUNKEN,
    borderwidth=5,
    command=wishMe
).pack(side=TOP,pady=30)


fever=IntVar()
age=IntVar()
pain=IntVar()
runnyNose=IntVar()
diffBreath=IntVar()

frame1=Frame(ws,bg='#5d8a82')
lab1=Label(frame1,text="FEVER:",padx=20,pady=20,bg='#5d8a82',font=("Helvetica 20 bold"),).pack(side=LEFT)
screen1 = Entry(frame1, textvar=fever, font=("lucida 14 italic"), bg='#5d8a82', borderwidth=6, relief=SUNKEN)
screen1.pack(ipady=15, padx=15, pady=10)
frame1.pack(padx=10)

frame2=Frame(ws,bg='#5d8a82')
lab2=Label(frame2,text="PAIN:",padx=20,pady=20,bg='#5d8a82',font=("Helvetica 20 bold"),).pack(side=LEFT)
R1 = Radiobutton(frame2, text="No Pain", variable=pain, value=0,font="Helvetica 14 bold",bg='#5d8a82')
R1.pack(side=LEFT)
R2 = Radiobutton(frame2, text="Severe Pain", variable=pain, value=1,font="Helvetica 14 bold",bg='#5d8a82')
R2.pack(side=LEFT)
frame2.pack(padx=10)

frame3=Frame(ws,bg='#5d8a82')
lab3=Label(frame3,text="AGE:",padx=20,pady=20,bg='#5d8a82',font=("Helvetica 20 bold"),).pack(side=LEFT)
screen3 = Entry(frame3, textvar=age, font=("lucida 14 italic"), borderwidth=6, relief=SUNKEN,bg='#5d8a82')
screen3.pack(ipady=15, padx=15, pady=10)
frame3.pack(padx=10)

frame4=Frame(ws,bg='#5d8a82')
lab4=Label(frame4,text="RUNNY NOSE:",padx=20,pady=20,bg='#5d8a82',font=("Helvetica 20 bold"),).pack(side=LEFT)
R3 = Radiobutton(frame4, text="Yes", variable=runnyNose, value=0,font="Helvetica 14 bold",bg='#5d8a82')
R3.pack(side=LEFT)
R4 = Radiobutton(frame4, text="No", variable=runnyNose, value=1,font="Helvetica 14 bold",bg='#5d8a82')
R4.pack(side=LEFT)
frame4.pack(padx=10)

frame5=Frame(ws,bg='#5d8a82')
lab5=Label(frame5,text="BREATHING DIFFICULTY:",padx=20,pady=20,bg='#5d8a82',font=("Helvetica 20 bold"),).pack(side=LEFT)
R5 = Radiobutton(frame5, text="No Difficulty", variable=diffBreath, value=-1,font="Helvetica 14 bold",bg='#5d8a82')
R5.pack(side=LEFT)
R6 = Radiobutton(frame5, text="Little Difficulty", variable=diffBreath, value=0,font="Helvetica 14 bold",bg='#5d8a82')
R6.pack(side=LEFT)
R7 = Radiobutton(frame5, text="Severe Difficulty", variable=diffBreath, value=1,font="Helvetica 14 bold",bg='#5d8a82')
R7.pack(side=LEFT)
frame5.pack(padx=10)

def result():
    inputFeatures = [fever.get(), pain.get(), age.get(), runnyNose.get(), diffBreath.get()]
    infProb = clf.predict_proba([inputFeatures])[0][1]
    speak("Your Probability of infection is")
    speak(round(infProb*100))
    speak("percent")


button5=Button(
    ws,
    text="Submit",
    font=("Helvetica 25 bold"),
    bg="orange",
    relief=SUNKEN,
    borderwidth=5,
    command=result
).pack(side=TOP,pady=30)


button6=Button(
    ws,
    text="Previous Page",
    font=f,
    command=prevPage,relief=SUNKEN,borderwidth=5
).pack(expand=TRUE, side=LEFT)

button7=Button(
    ws,
    text="START NOW",
    font=f,
    command=nextPage,
    bg="green",relief=SUNKEN,borderwidth=5
).pack(expand=TRUE, side=RIGHT)
ws.mainloop()