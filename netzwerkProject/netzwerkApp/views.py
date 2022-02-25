from django.shortcuts import render
from datetime import datetime
from netzwerkApp.models import MyModel, MyChild
from django.http import HttpResponse
#Create your views here.
def hello(request):
    today = datetime.now().date()
    daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    return render(request, "Child.html", {"today" : today, "days_of_week" : daysOfWeek}) 

from django.http import HttpResponse
def dbops(request):
    objects = MyModel.objects.all() 
    for elt in objects:
        elt.delete()
    #Creating an entry
    myChild = MyChild( domain ="polo.com")
    myChild.save()    
    myModel = MyModel( website = "www.polo.com", mail = "sorex@polo.com", name = "sorex",  phonenumber = "002376970" , mychild = myChild )
    myModel.save()
    myModel = MyModel( website = "www.netzwerk.com", mail = "test@netzwerk.com", name = "karthikeya",  phonenumber = "123456789", mychild = myChild )
    myModel.save()
    #Read ALL entries 
    objects = MyModel.objects.all() 
    res ='Printing all MyModel entries in the DB : <br>' 
    for elt in objects: res += elt.name+"<br>" 
    #Read a specific entry:
    sorex = MyModel.objects.get(name = "sorex") 
    res += 'Printing One entry <br>' 
    res += sorex.name + '<br>'
    res += sorex.mychild.domain     
    #Delete an entry 
    res += '<br> Deleting an entry <br>'
    sorex.delete()
    #Update
    myModel = MyModel( website = "www.netzwerk.com", mail = "test1@netzwerk.com", name = "Srisam", phonenumber = "456789" , mychild = myChild) 
    myModel.save() 
    res += 'Updating entry<br>' 
    myModel = MyModel.objects.get(name = 'karthikeya') 
    myModel.name = 'Sri' 
    myModel.save() 
    res += myModel.name 
    return HttpResponse(res) 

def modelFilter(request):
  res = '' 
  #Filtering data: 
  qs = MyModel.objects.filter(name = "Srisam")
  res += "Found : %s results<br>"%len(qs)
  #Ordering results
  qs = MyModel.objects.order_by("name") 
  for elt in qs:
    res += elt.name + '<br>' 
  return HttpResponse(res) 


    