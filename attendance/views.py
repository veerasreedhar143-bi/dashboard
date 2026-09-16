from django.shortcuts import render

# Create your views here.
def attendance_details(request):
    return render(request,"attendance/attendance.html")

def attendance_calendar(request):
    return render(request,"attendance/calendar.html")
