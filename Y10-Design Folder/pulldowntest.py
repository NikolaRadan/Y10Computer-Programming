from tkinter import *
import webbrowser 


def OpenUrl():
    webbrowser.open_new(url)

def OpenUrl2():
    webbrowser.open_new(url2)

master = Tk()
    
url= "file:///Users/nikola.radan/Documents/Y10-Design%20Folder/stock.html"
url2="https://go.teamsnap.com/841751/schedule?mode=list"

button = Button(master, text="VEEV Stock", command=OpenUrl)
button.pack()

button2 = Button(master, text="AAPL Stock", command=OpenUrl2)
button2.pack()

mainloop()
