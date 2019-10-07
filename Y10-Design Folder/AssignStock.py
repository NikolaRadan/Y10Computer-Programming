import requests

myrequest=requests.get("https://api.worldtradingdata.com/api/v1/stock?symbol=VEE.F&api_token=LR1vMZpzySAxp2C30GtVNzo7FCgNCkDMue8Bq52EeXJQ0kwsLD4KAYtTKq0w")
datajson=myrequest.json()

#ALL DATA FOR VEEV
data=datajson['data']
#pricecdata
price=data[0]['price']
#dailyhigh data
dayhigh=data[0]['day_high']
#day low
daylow=data[0]['day_low']
#52week high
fiftyhigh=data[0]['52_week_high']
#52week low
fiftylow=data[0]['52_week_low']


#ALL DATA FOR AAPL
#dataAAPL=datajson['data']
#pricecdata
#priceAAPL=dataAAPL[0]['price']
#dailyhigh data
#dayhighAAPL=dataAAPL[0]['day_high']
#day low
#daylowAAPL=dataAAPL[0]['day_low']
#52week high
#fiftyhighAAPL=dataAAPL[0]['52_week_high']
#52week low
#fiftylowAAPL=dataAAPL[0]['52_week_low']



#WEBSITE VEEV
ofile=open("stock.html","w")
ofile.write("<h2>" + "price is:" + price + "</h2>")
ofile.write("<h2>" + "The Day high was:" + dayhigh + "</h2>")
ofile.write("<h2>" + "The Day high was:" + dayhigh + "</h2>")
ofile.write("<h2>" + "The Day low was:" + daylow + "</h2>")
ofile.write("<h2>" + "The 52 week high is:" + fiftyhigh + "</h2>")
ofile.write("<h2>" + "The 52 week low is:" + fiftylow + "</h2>")
ofile.write("<button onclick='runme()'>click me</button>")
ofile.write("<script>function runme() { alert('this is a test') }</script>")


ofile.close()
