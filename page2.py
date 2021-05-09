from tkinter import *
from tkPDFViewer import tkPDFViewer as pdf
ws = Tk()
width, height = ws.winfo_screenwidth(), ws.winfo_screenheight()
ws.geometry('%dx%d+0+0' % (width,height))
ws.title("Your Home Quarantine Guide")
ws['bg'] = '#5d8a82'
f = ("Times bold", 14)

def nextPage():
    ws.destroy()
    import page3

def prevPage():
    ws.destroy()
    import page1

v1 = pdf.ShowPdf()
v2 = v1.pdf_view(ws,
                 pdf_location=r"D:\\frosthack2021\\images\\050802545085.pdf",
                 width=150, height=40)
v2.pack(side=TOP,pady=20)

button2=Button(
    ws,
    text="Previous Page",
    font=f,
    command=prevPage,relief=SUNKEN,borderwidth=5
).pack(expand=TRUE, side=LEFT)

button3=Button(
    ws,
    text="Next Page",
    font=f,
    command=nextPage,
    bg="green",relief=SUNKEN,borderwidth=5
).pack(expand=TRUE, side=RIGHT)
ws.mainloop()