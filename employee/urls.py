from django.urls import path
from employee.views import *

urlpatterns = [

    path('employee/',employee_details),
    path('employee_list/',employee_list),
    path('add_edit_employee/',add_edit_employee),
    path('employee_profile/',employee_profile),
    path('profile_details/<int:id>/',profile_details),


]
