from django.shortcuts import render, redirect
from accounts.models import UserRegister
# Create your views here.
def register(request):

    if request.method == "POST":

        first = request.POST.get("first_name")
        last = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        mobile = request.POST.get("mobile")
        gender = request.POST.get("gender")

        UserRegister.objects.create(
            first_name=first,
            last_name=last,
            email=email,
            password=password,
            mobile=mobile,
            gender=gender
        )

        return redirect("login")

    return render(request, "accounts/register.html")

def login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = UserRegister.objects.get(email=username, password=password)

            request.session["user"] = user.id

            return redirect("homepage")

        except UserRegister.DoesNotExist:

            return render(request,"accounts/login.html",{
                "error":"Invalid Email or Password"
            })

    return render(request,"accounts/login.html")
