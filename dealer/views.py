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