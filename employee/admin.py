from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'employee_name',
        'employee_id',
        'phone',
        'address',
        'job_role',
        'department',
        'joining_date',
        'experience',
        'skills',
        'resume',
    ]

admin.site.register(Employee, EmployeeAdmin)
