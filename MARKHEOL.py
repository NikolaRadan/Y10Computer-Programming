import requests
from tkinter import *
import webbrowser
from PIL import ImageTk, Image

def getStuff():
    request = requests.get("https://api.worldtradingdata.com/api/v1/stock?symbol=" + e1.get() + "&api_token=LR1vMZpzySAxp2C30GtVNzo7FCgNCkDMue8Bq52EeXJQ0kwsLD4KAYtTKq0w")
    datajson = request.json()
    print(str(datajson))
    writeitOut(datajson)

def writeitOut(datajson):
    dataAAPL=datajson['data']
    #pricecdata
    priceAAPL=dataAAPL[0]['price']
    #dailyhigh data
    dayhighAAPL=dataAAPL[0]['day_high']
    #day low
    daylowAAPL=dataAAPL[0]['day_low']
    #52week high
    fiftyhighAAPL=dataAAPL[0]['52_week_high']
    #52week low
    fiftylowAAPL=dataAAPL[0]['52_week_low']
    ofile=open("poopypants.html","w")
    ofile.write("<head> <link rel='stylesheet' href 'style.css'> </head>")
    ofile.write("<body style='background-color:powderblue;'>")
    ofile.write("<p style='font-size:50px; text-align:center; font-family:verdana;'> Your Stock Data </p>")
    ofile.write("<center><img src='download-1.png' alt='Trulli' width='200' height='200' style=text-align:center;></center>")
    ofile.write("<p style= text-align:center;>" + "Price is: $" + priceAAPL + "</p>")
    ofile.write("<p style= text-align:center;>" + "The Day high was: $" + dayhighAAPL + "</p>")
    ofile.write("<p style= text-align:center;>" + "The Day low was: $" + daylowAAPL + "</font>" + "</p>")
    ofile.write("<p style= text-align:center;>" + "The 52 week high is: $" + fiftyhighAAPL + "</p>")
    ofile.write("<p style= text-align:center;>" + "The 52 week low is: $" + fiftylowAAPL + "</p>")
    ofile.write("</body>")
    ofile.close()

def openIt():
    webbrowser.open("file:///Users/nikola.radan/Documents/Y10-Design%20Folder/poopypants.html")
    
win=Tk()
titleframe = Frame(win,width=200,height=200, bg="#e39b17") # top title frame
titleframe.grid(row=2,column=0)
e1=Entry(titleframe)
b1=Button(titleframe,text="get data", command=getStuff)
b2=Button(titleframe,text="website",command=openIt)
e1.grid(row=2,column=0)
b1.grid(row=3,column=0)
b2.grid(row=4,column=0)
Label_1=Label(win, text="Welcome to my Stock interface!", bg="blue", fg="white", font="Verdana 32 bold italic")
Label_1.grid(row=0,column=0)
Label_1=Label(win, text="Chose a stock!", bg="blue", fg="white", font="Verdana 10 bold italic")
Label_1.grid(row=1,column=0)
img = ImageTk.PhotoImage(Image.open("download-1.png"))
panel = Label(win, image = img)
panel.grid(row=6, column=0)




