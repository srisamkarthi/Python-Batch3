from django.shortcuts import render
from StudentDetailsApp.models import Student
# Create your views here.
def student(request):
    student = Student(name="karthikeya", section ="A" ,sno ="KA1234", phonenumber ="98888888")
    student.save()
    return render(request, "student.html", {"Student" : student}) 
