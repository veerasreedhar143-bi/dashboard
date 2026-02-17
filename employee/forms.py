from django import forms
from employee.models import Employee
class Employee_mode_form(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
