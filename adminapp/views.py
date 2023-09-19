from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from website.forms import LoginForm
from website.forms import AgentRegistration
from website.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

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
            return redirect("adminapp:index")
    return render(request,'adminapp/add_agent.html',{"login_form": login_form, "agent_form": agent_form})

def dealer(request):
    return render(request,'adminapp/customer/dealer.html')

def change_game(request):
    return render(request,'adminapp/changegame.html')

def monitor(request):
    return render(request,'adminapp/monitor.html')

def results(request):
    return render(request,'adminapp/results.html')

def dailyreport(request):
    return render(request,'adminapp/dailyreport.html')

def changepassword(request):
    return render(request,'adminapp/changepassword.html')

