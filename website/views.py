from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import User
from django.contrib.auth import authenticate,login as auth_login
from django.contrib.auth import login,logout
from django.contrib import messages

# Create your views here.


@csrf_exempt
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            messages.success(request, "Both Username and Password Required")
            return redirect("/")

        user_obj = User.objects.filter(username=username).first()
        if user_obj is None:
            messages.success(request, "User not found")
            return redirect("/")

        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.success(request, "Wrong Paasword")
            return redirect("/")

        if user:
            auth_login(request,user)

            if user.is_staff:
                return redirect("adminapp:index")
            elif user.is_agent:
                return redirect("agent:index")
            elif user.is_dealer:
                return redirect("dealer:index")
        else:
            messages.info(request, "Invalid Credentials")
    return render(request,'website/login.html')