from django.shortcuts import render
from django.http import HttpResponse
from employee.models import Employee
from employee.forms import Employee_mode_form

# Create your views here.
def homepage(request):
    return render(request,"employee/base.html")

# employee view
def employee_details(request):
    return render(request,"employee/employee.html")

def employee_list(request):
    employees = Employee.objects.all()
    employee_list={'employees':employees}
    return render(request,"employee/employee_list.html",employee_list)

def add_edit_employee(request):
    employees=Employee.objects.all()
    e={'employees':employees}
    return render(request,"employee/add_edit_employee.html",e)

def employee_profile(request):
    employees = Employee.objects.all()
    return render(request,'employee/employee_profile.html',{'employees':employees})


def profile_details(request,id):
    emp = Employee.objects.get(id=id)
    return render(request,'employee/employee_profile_card.html',{'emp':emp})
