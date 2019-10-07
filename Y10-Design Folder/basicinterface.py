from tkinter import *

def printme():
    print(et1.get())

win = Tk()
win.geometry('400x400')

et1 = Entry(win)
et1.grid(row=0,column=0)
et2 = Entry(win)
et2.grid(row=0,column=1)

b1 = Button(win,text="Print et1",command=printme)
b1.grid(row=1,column=0)
