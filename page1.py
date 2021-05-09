from tkinter import *
from PIL import ImageTk, Image
ws = Tk()
width, height = ws.winfo_screenwidth(), ws.winfo_screenheight()
ws.geometry('%dx%d+0+0' % (width,height))
ws.title("Your Home Quarantine Guide")
ws['bg'] = '#5d8a82'
f = ("Times bold", 14)

def nextPage():
    ws.destroy()
    import page2

def prevPage():
    ws.destroy()
    import page3

label1=Label(
    ws,
    text="WELCOME TO YOUR HOME QUARANTINE GUIDE",
    padx=20,
    pady=20,
    bg='yellow',
    font=("Helvetica 45 bold"),
).pack(fill=X , anchor="nw",ipady=40)

label2=Label(
    ws,
    text="DON'T PANIC WE ARE WITH YOU,YOU WILL BE ALRIGHT:-)",
    padx=20,
    pady=20,
    bg='#5d8a82',
    font=("Helvetica 20 bold"),
).pack(side=TOP,fill=X )

image1 = Image.open('images/main.png')
image1 = image1.resize((600,400), Image.ANTIALIAS)
my_img1 = ImageTk.PhotoImage(image1)
label3=Label(
    ws,image=my_img1
).pack(side=TOP)

button1=Button(
    ws,
    text="READ THE INSTRUCTIONS>>",
    font=f,
    command=nextPage,
    relief=SUNKEN,borderwidth=5
).pack(side=RIGHT,padx=10)

ws.mainloop()