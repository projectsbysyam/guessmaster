from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from website.decorators import dealer_required, agent_required, admin_required
from website.forms import LoginForm,UserUpdateForm
from website.forms import AgentRegistration
from website.models import User,Agent,Dealer
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@admin_required
@login_required
def index(request):
    return render(request,'adminapp/index.html')

def agent(request):
    return render(request,'adminapp/customer/agent.html')

@csrf_exempt
def add_agent(request):
    login_form = LoginForm()
    agent_form = AgentRegistration()
    if request.method == "POST":
        agent_form = AgentRegistration(request.POST)
        login_form = LoginForm(request.POST)
        print(agent_form)
        print(login_form)
        if login_form.is_valid() and agent_form.is_valid():
            print("loginform is not working")
            user = login_form.save(commit=False)
            user.is_agent = True
            user.save()
            c = agent_form.save(commit=False)
            c.user = user
            c.save()
            messages.info(request, "Agent Created Successfully")
            return redirect("adminapp:view_agent")
    return render(request,'adminapp/add_agent.html',{"login_form": login_form, "agent_form": agent_form})

def view_agent(request):
    agents = Agent.objects.filter().all()
    context = {
        'agents' : agents
    }
    return render(request,'adminapp/view_agent.html',context)

def edit_agent(request,id):
    agent = get_object_or_404(Agent, id=id)
    user = agent.user
    if request.method == "POST":
        agent_form = AgentRegistration(request.POST, instance=agent)
        login_form = UserUpdateForm(request.POST, instance=user)
        if agent_form.is_valid() and login_form.is_valid():
            agent_form.save()
            messages.info(request, "Agent Updated Successfully")
            return redirect("adminapp:view_agent")
    else:
        agent_form = AgentRegistration(instance=agent)
        login_form = UserUpdateForm(instance=user)
    return render(request, 'adminapp/edit_agent.html', {'agent': agent,'agent_form': agent_form,'login_form':login_form})

def delete_agent(request,id):
    agent = get_object_or_404(Agent, id=id)
    agent_user = agent.user
    dealers = Dealer.objects.filter(agent=agent)
    for dealer in dealers:
        dealer_user = dealer.user
        dealer_user.delete()
    agent_user.delete()
    return redirect('adminapp:view_agent')

def ban_agent(request,id):
    agent = get_object_or_404(Agent, id=id)
    user = agent.user
    user.is_active = False
    user.save()
    dealers = Dealer.objects.filter(agent=agent)
    for dealer in dealers:
        dealer_user = dealer.user
        dealer_user.is_active = False
        dealer_user.save()
        print(dealer_user.is_active)
    return redirect('adminapp:view_agent')

def remove_ban(request,id):
    agent = get_object_or_404(Agent, id=id)
    user = agent.user
    user.is_active = True
    user.save()
    dealers = Dealer.objects.filter(agent=agent)
    for dealer in dealers:
        dealer_user = dealer.user
        dealer_user.is_active = True
        dealer_user.save()
        print(dealer_user.is_active)
    return redirect('adminapp:view_agent')

def package(request):
    return render(request,'adminapp/package.html')

def new_package(request):
    return render(request,'adminapp/new_package.html')

def create_winningprice(request):
    return render(request,'adminapp/create_winningprice.html')


def sales_report(request):
    return render(request,'adminapp/sales_report.html')


def change_game(request):
    return render(request,'adminapp/changegame.html')

def monitor(request):
    return render(request,'adminapp/monitor.html')

def results(request):
    return render(request,'adminapp/results.html')

def daily_report(request):
    return render(request,'adminapp/dailyreport.html')

