from django.shortcuts import render
from EmpDetailsApp.models import Employee
# Create your views here.
def emp(request):
    employee = Employee(name="karthikeya", phonenumber ="98888888")
    employee.save()
    return render(request, "employee.html", {"Employee" : employee}) 