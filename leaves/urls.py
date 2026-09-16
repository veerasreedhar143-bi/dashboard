from django.urls import path
from leaves.views import *

urlpatterns = [

    path('apply_leaves/',apply_leaves),
]
