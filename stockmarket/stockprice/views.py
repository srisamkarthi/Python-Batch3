from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from stockprice.models import sprice,market

def hello(request):
    text = """<h1>welcome to netzwerk app !</h1>"""
    return HttpResponse(text) 
def greetings(request):
    today = datetime.now().date()
    daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    return render(request, "stockprice.html", {"today":today,"days_of_week":daysOfWeek})
def dbops(request):
 #Creating an entry
 mkt = market(name ="USA", city="New York")
 mkt.save()
 myModel = sprice( stockName = "Tata", stockType = "Mutual Funds", exchangeName = "BSE",  stockPrice = 200, market = mkt)
 myModel.save()
 #Read ALL entries 
 #objects = sprice.objects.all() 
 res ='Printing entries in the DB : <br>' 
 #for elt in objects: res += elt.stockName+"<br>" + elt.stockType+"<br>"+ elt.exchangeName+"<br>" + str(elt.stockPrice) +"<br>" 
 #Read a specific entry:
 elt = sprice.objects.get(stockName = "Tata") 
 elt.stockName ="TCS"
 elt.save()
 res += "Printing One entry <br>"+ elt.stockName+"<br>" + elt.stockType+"<br>"+ elt.exchangeName+"<br>" + str(elt.stockPrice) +"<br>" 
 #Delete an entry 
 #res += '<br> Deleting an entry <br>' sorex.delete() 
 #Update myModel = MyModel( website = "www.polo.com", mail = "sorex@polo.com", name = "sorex", phonenumber = "002376970" ) 
 #myModel.save() 
 #res += 'Updating entry<br>' 
 #myModel = myModel.objects.get(name = 'sorex') 
 #myModel.name = 'thierry' 
 #dreamreal.save() 
 return HttpResponse(res)
def datafilter(request):
  res = '' 
  #Filtering data: 
  qs = sprice.objects.filter(exchangeName = "BSE")
  res += "Found : %s results<br>"%len(qs)
  #Ordering results
  qs = sprice.objects.order_by("exchangeName") 
  for elt in qs:
    res += elt.stockName+"<br>" + elt.stockType+"<br>"+ elt.exchangeName+"<br>" + str(elt.stockPrice) +"<br>" + elt.market.name +"<br>" + elt.market.city +"<br>"
  return HttpResponse(res) 
 
    

