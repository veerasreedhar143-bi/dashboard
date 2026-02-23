from django.urls import path
from employee.views import *

urlpatterns = [

    path('employee/', employee_details),
    path('employee_list/', employee_list, name='employee_list'),
    path('add_edit_employee/', add_edit_employee),
    path('employee_profile/', employee_profile),
    path('profile_details/<int:id>/',
         profile_details,
         name='profile_details'),
    path('employee_details/<int:id>/',
         employee_all_details,
         name='employee_details'),



    # crud operation
    path('delete_employee/<int:id>/', delete_employee),
    path('update_employee/<int:id>/', update_employee),

]
