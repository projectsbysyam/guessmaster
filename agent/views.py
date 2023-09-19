from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from website.forms import LoginForm
from website.forms import DealerRegistration
from website.models import User,Dealer
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@login_required
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
            print("loginform is working")
            user = login_form.save(commit=False)
            user.is_dealer = True
            user.save()
            c = dealer_form.save(commit=False)
            c.user = user
            c.save()
            messages.info(request, "Dealer Created Successfully")
            return redirect("agent:view_dealer")
    return render(request,'agent/add_dealer.html',{"login_form": login_form, "dealer_form": dealer_form})

def view_dealer(request):
    dealers = Dealer.objects.filter().all()
    context = {
        'dealers' : dealers
    }
    return render(request,'agent/view_dealer.html',context)
