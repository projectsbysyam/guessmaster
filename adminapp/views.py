from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'adminapp/index.html')

def agent(request):
    return render(request,'adminapp/customer/agent.html')

def addagent(request):
    return render(request,'adminapp/customer/addagent.html')

def dealer(request):
    return render(request,'adminapp/customer/dealer.html')

def changegame(request):
    return render(request,'adminapp/changegame.html')

def monitor(request):
    return render(request,'adminapp/monitor.html')

def results(request):
    return render(request,'adminapp/results.html')

def dailyreport(request):
    return render(request,'adminapp/dailyreport.html')

def changepassword(request):
    return render(request,'adminapp/changepassword.html')


