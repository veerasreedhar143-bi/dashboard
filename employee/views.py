from django.shortcuts import render, redirect, get_object_or_404
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
    selected_emp = None

    emp_id = request.GET.get('id')

    if emp_id:
        selected_emp = get_object_or_404(Employee, id=emp_id)

    context = {'employees': employees,'selected_emp': selected_emp  }

    return render(request,'employee/employee_list.html', context)

def delete_employee(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('employee/employee_list.html/')

def update_employee(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, "employee/add_edit_employee.html", {'employee': employee})

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

def employee_all_details(request, id):
    selected_emp = get_object_or_404(Employee, id=id)
    return render(request,'employee/employee_all_details.html',{'selected_emp': selected_emp})
