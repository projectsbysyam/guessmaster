from django.shortcuts import render
from website.decorators import dealer_required, agent_required
from django.contrib.auth.decorators import login_required

# Create your views here.
@dealer_required
@login_required
def index(request):
    return render(request,"dealer/index.html")



def booking(request):
    return render(request,'dealer/booking.html')

def result(request):
    return render(request,'dealer/results.html')

def edit_bill(request):
    return render(request,'dealer/edit_bill.html')

def sales_report(request):
    return render(request,'dealer/sales_report.html') 

def daily_report(request):
    return render(request,'dealer/daily_report.html')

def winning_report(request):
    return render(request,'dealer/winning_report.html') 
def count_salereport(request):
    return render(request,'dealer/count_salereport.html') 

def winning_countreport(request):
    return render(request,'dealer/winning_countreport.html') 

def balance_report(request):
    return render(request,'dealer/balance_report.html') 