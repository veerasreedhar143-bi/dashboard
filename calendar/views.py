from django.shortcuts import render

def calendar_home(request):
    return render(request, 'calendar/calendar.html')
