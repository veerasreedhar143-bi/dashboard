from django.urls import path
from calendar.views import *

urlpatterns = [

    path('calendar/',calendar_home),
]
