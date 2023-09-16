from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'adminapp/index.html')

def agent(request):
    return render(request,'adminapp/customer/agent.html')

def dealer(request):
    return render(request,'adminapp/customer/dealer.html')

def changegame(request):
    return render(request,'adminapp/changegame.html')



