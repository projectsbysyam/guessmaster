from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from website.forms import LoginForm
from website.forms import DealerRegistration,UserUpdateForm
from website.models import User,Dealer,Agent
from adminapp.models import PlayTime
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from website.decorators import dealer_required, agent_required
from django.utils import timezone
from pytz import timezone as pytz_timezone

# Create your views here.
@login_required
@agent_required
def index(request):
    times = PlayTime.objects.filter().all()
    ist = pytz_timezone('Asia/Kolkata')
    current_time = timezone.now().astimezone(ist).time()
    print(current_time)
    game_times = [time.time for time in PlayTime.objects.all()]
    print(game_times)
    one_hour_before_times = [(t.replace(hour=t.hour - 1) if t.hour > 0 else t.replace(hour=23, minute=0)) for t in game_times]
    print(one_hour_before_times)
    available_games = []
    for game_time, one_hour_before in zip(game_times, one_hour_before_times):
        if current_time >= one_hour_before:
            available_games.append(game_time)
    print("Hiiii")
    context = {
        'times' : times,
        'current_time' : current_time,
        'game_available' : available_games
    }
    return render(request,"agent/index.html",context)

@csrf_exempt
def add_dealer(request):
    login_form = LoginForm()
    dealer_form = DealerRegistration()
    agent_obj = Agent.objects.get(user=request.user)
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
            dealer = dealer_form.save(commit=False)
            dealer.user = user
            dealer.agent = agent_obj  # Associate the agent_obj with the dealer
            dealer.save()
            messages.info(request, "Dealer Created Successfully")
            return redirect("agent:view_dealer")
    return render(request,'agent/add_dealer.html',{"login_form": login_form, "dealer_form": dealer_form})

def view_dealer(request):
    agent = Agent.objects.get(user=request.user)
    print(agent)
    dealers = Dealer.objects.filter(agent=agent).all()
    context = {
        'dealers' : dealers
    }
    return render(request,'agent/view_dealer.html',context)

def edit_dealer(request,id):
    dealer = get_object_or_404(Dealer, id=id)
    user = dealer.user
    if request.method == "POST":
        dealer_form = DealerRegistration(request.POST, instance=dealer)
        login_form = UserUpdateForm(request.POST, instance=user)
        if dealer_form.is_valid() and login_form.is_valid():
            dealer_form.save()
            messages.info(request, "Dealer Updated Successfully")
            return redirect("agent:view_dealer")
    else:
        dealer_form = DealerRegistration(instance=dealer)
        login_form = UserUpdateForm(instance=user)
    return render(request, 'agent/edit_dealer.html', {'dealer': dealer,'dealer_form': dealer_form,'login_form':login_form})


def delete_dealer(request,id):
    dealer = get_object_or_404(Dealer, id=id)
    dealer_user = dealer.user
    dealer_user.delete()
    return redirect('agent:view_dealer')

def ban_dealer(request,id):
    dealer = get_object_or_404(Dealer, id=id)
    user = dealer.user
    user.is_active = False
    user.save()
    return redirect('agent:view_dealer')

def remove_ban(request,id):
    dealer = get_object_or_404(Dealer,id=id)
    user = dealer.user
    user.is_active = True
    user.save()
    return redirect('agent:view_dealer')

def booking(request):
    return render(request,'agent/booking.html')