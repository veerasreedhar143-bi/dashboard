from django.urls import path
from attendance.views import *

urlpatterns = [

    path('attendance/',attendance_details),
    path('calendar/',attendance_calendar),
]
