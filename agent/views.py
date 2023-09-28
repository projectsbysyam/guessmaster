from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from website.forms import LoginForm
from website.forms import DealerRegistration,UserUpdateForm
from website.models import User,Dealer,Agent
from adminapp.models import PlayTime
from .models import DealerPackage
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from website.decorators import dealer_required, agent_required
from django.utils import timezone
from pytz import timezone as pytz_timezone

# Create your views here.
@login_required
@agent_required
def index(request):
    ist = pytz_timezone('Asia/Kolkata')
    current_time = timezone.now().astimezone(ist).time()
    print(current_time)
    play_times = PlayTime.objects.filter().all()
    play_time_availabilities = []
    for time in play_times:
        if time.start_time <= current_time <= time.end_time:
            play_time_availabilities.append(True)
        else:
            play_time_availabilities.append(False)
    zipped_play_times = zip(play_times, play_time_availabilities)
    context = {
        'play_times': play_times,
        'zipped_play_times': zipped_play_times,
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



def results(request):
    return render(request,'agent/results.html')

def sales_report(request):
    return render(request,'agent/sales_report.html')

def daily_report(request):
    return render(request,'agent/daily_report.html')

def winning_report(request):
    return render(request,'agent/winning_report.html') 

def count_salereport(request):
    return render(request,'agent/count_salereport.html') 

def winning_countreport(request):
    return render(request,'agent/winning_countreport.html') 

def collection_report(request):
    return render(request,'agent/collection_report.html') 

def add_collection(request):
    return render(request,'agent/add_collection.html') 

def balance_report(request):
    return render(request,'agent/balance_report.html') 

def edit_bill(request):
    return render(request,'agent/edit_bill.html')

def change_password(request):
    return render(request,'agent/change_password.html')
def play_game(request,id):
    print(id)
    time = PlayTime.objects.get(id=id)
    print(time.end_time)
    agent = Agent.objects.get(user=request.user)
    dealers = Dealer.objects.filter(agent=agent).all()
    context = {
        'time' : time,
        'dealers' : dealers
    }
    return render(request,'agent/play_game.html',context)



def package(request):
    packages = DealerPackage.objects.filter().all()
    print(packages)
    context = {
        'packages' : packages
    }
    return render(request,'agent/package.html',context)

def new_package(request):
    user_obj = request.user
    try:
        dealer = Dealer.objects.filter().all()
    except:
        pass
    if request.method == 'POST':
        dealer_obj = request.POST.get('dealer')
        package_name = request.POST.get('package_name')
        single_rate = request.POST.get('single_rate')
        single_dc = request.POST.get('single_dc')
        double_rate = request.POST.get('double_rate')
        double_dc = request.POST.get('double_dc')
        box_rate = request.POST.get('box_rate')
        box_dc = request.POST.get('box_dc')
        super_rate = request.POST.get('super_rate')
        super_dc = request.POST.get('super_dc')
        first_prize = request.POST.get('first_prize')
        first_dc = request.POST.get('first_dc')
        second_prize = request.POST.get('second_prize')
        second_dc = request.POST.get('second_dc')
        third_prize = request.POST.get('third_prize')
        third_dc = request.POST.get('third_dc')
        fourth_prize = request.POST.get('fourth_prize')
        fourth_dc = request.POST.get('fourth_dc')
        fifth_prize = request.POST.get('fifth_prize')
        fifth_dc = request.POST.get('fifth_dc')
        guarantee_prize = request.POST.get('guarantee_prize')
        guarantee_dc = request.POST.get('guarantee_dc')
        box_first_prize = request.POST.get('box_first_prize')
        box_first_prize_dc = request.POST.get('box_first_prize_dc')
        box_series_prize = request.POST.get('box_series_prize')
        box_series_dc = request.POST.get('box_series_dc')
        single1_prize = request.POST.get('single1_prize')
        single1_dc = request.POST.get('single1_dc')
        double2_prize = request.POST.get('double2_prize')
        double2_dc = request.POST.get('double2_dc')
        selected_dealer = Dealer.objects.get(id=dealer_obj)
        if DealerPackage.objects.filter(dealer=dealer_obj).exists():
            messages.info(request, "Package is not set, This dealer already have a package!")
        else:
            add_package = DealerPackage.objects.create(dealer=selected_dealer,created_by=user_obj,package_name=package_name,single_rate=single_rate,
                        single_dc=single_dc,double_rate=double_rate,double_dc=double_dc,box_rate=box_rate,
                        box_dc=box_dc,super_rate=super_rate,super_dc=super_dc,first_prize=first_prize,first_dc=first_dc,
                        second_prize=second_prize,second_dc=second_dc,third_prize=third_prize,third_dc=third_dc,fourth_prize=fourth_prize,
                        fourth_dc=fourth_dc,fifth_prize=fifth_prize,fifth_dc=fifth_dc,guarantee_prize=guarantee_prize,
                        guarantee_dc=guarantee_dc,box_first_prize=box_first_prize,box_first_prize_dc=box_first_prize_dc,
                        box_series_prize=box_series_prize,box_series_dc=box_series_dc,single1_prize=single1_prize,
                        single1_dc=single1_dc,double2_prize=double2_prize,double2_dc=double2_dc)
            add_package.save()
            messages.info(request, "Package created successfully!")
            return redirect('agent:package')
    context = {
        'dealers' : dealer
    }
    return render(request,'agent/new_package.html',context)

def edit_package(request,id):
    package = DealerPackage.objects.get(id=id)
    user_obj = request.user
    if request.method == 'POST':
        dealer_obj = request.POST.get('dealer')
        package_name = request.POST.get('package_name')
        single_rate = request.POST.get('single_rate')
        single_dc = request.POST.get('single_dc')
        double_rate = request.POST.get('double_rate')
        double_dc = request.POST.get('double_dc')
        box_rate = request.POST.get('box_rate')
        box_dc = request.POST.get('box_dc')
        super_rate = request.POST.get('super_rate')
        super_dc = request.POST.get('super_dc')
        first_prize = request.POST.get('first_prize')
        first_dc = request.POST.get('first_dc')
        second_prize = request.POST.get('second_prize')
        second_dc = request.POST.get('second_dc')
        third_prize = request.POST.get('third_prize')
        third_dc = request.POST.get('third_dc')
        fourth_prize = request.POST.get('fourth_prize')
        fourth_dc = request.POST.get('fourth_dc')
        fifth_prize = request.POST.get('fifth_prize')
        fifth_dc = request.POST.get('fifth_dc')
        guarantee_prize = request.POST.get('guarantee_prize')
        guarantee_dc = request.POST.get('guarantee_dc')
        box_first_prize = request.POST.get('box_first_prize')
        box_first_prize_dc = request.POST.get('box_first_prize_dc')
        box_series_prize = request.POST.get('box_series_prize')
        box_series_dc = request.POST.get('box_series_dc')
        single1_prize = request.POST.get('single1_prize')
        single1_dc = request.POST.get('single1_dc')
        double2_prize = request.POST.get('double2_prize')
        double2_dc = request.POST.get('double2_dc')
        selected_dealer = Dealer.objects.get(id=dealer_obj)
        add_package = DealerPackage.objects.update(dealer=selected_dealer,created_by=user_obj,package_name=package_name,single_rate=single_rate,
                        single_dc=single_dc,double_rate=double_rate,double_dc=double_dc,box_rate=box_rate,
                        box_dc=box_dc,super_rate=super_rate,super_dc=super_dc,first_prize=first_prize,first_dc=first_dc,
                        second_prize=second_prize,second_dc=second_dc,third_prize=third_prize,third_dc=third_dc,fourth_prize=fourth_prize,
                        fourth_dc=fourth_dc,fifth_prize=fifth_prize,fifth_dc=fifth_dc,guarantee_prize=guarantee_prize,
                        guarantee_dc=guarantee_dc,box_first_prize=box_first_prize,box_first_prize_dc=box_first_prize_dc,
                        box_series_prize=box_series_prize,box_series_dc=box_series_dc,single1_prize=single1_prize,
                        single1_dc=single1_dc,double2_prize=double2_prize,double2_dc=double2_dc)
        messages.info(request, "Package updated successfully!")
        return redirect('agent:package')
    context = {
        'package' : package
    }
    return render(request,'agent/edit_package.html',context)

def delete_package(request,id):
    package = DealerPackage.objects.get(id=id)
    package.delete()
    return redirect('agent:package')
