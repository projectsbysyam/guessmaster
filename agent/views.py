from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from website.forms import LoginForm
from website.forms import DealerRegistration
from website.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return render(request,"agent/index.html")

@csrf_exempt
def add_dealer(request):
    login_form = LoginForm()
    dealer_form = DealerRegistration()
    if request.method == "POST":
        dealer_form = DealerRegistration(request.POST)
        login_form = LoginForm(request.POST)
        print(dealer_form)
        print(login_form)
        if login_form.is_valid() and dealer_form.is_valid():
            print("loginform is not working")
            user = login_form.save(commit=False)
            user.is_dealer = True
            user.save()
            c = dealer_form.save(commit=False)
            c.user = user
            c.save()
            messages.info(request, "dealer Created Successfully")
            return redirect("adminapp:index")
    return render(request,'adminapp/add_dealer.html',{"login_form": login_form, "dealer_form": dealer_form})
