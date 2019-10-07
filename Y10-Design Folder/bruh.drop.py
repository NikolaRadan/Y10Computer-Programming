from tkinter import *

OPTIONS = [
"",
"Bruh",
"Cheese"
] #etc

master = Tk()

variable = StringVar(master)
variable.set(OPTIONS[0]) # default value

w = OptionMenu(master, variable, *OPTIONS)
w.pack()

def ok():
    print ("That Lasaugna is:" + variable.get())

button = Button(master, text="OK", command=ok)
button.pack()

mainloop()
