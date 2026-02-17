from django.urls import path
from attendance.views import attendance_details

urlpatterns = [

    path('attendance/',attendance_details),
]
