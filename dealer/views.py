from django.shortcuts import render
from website.decorators import dealer_required, agent_required
from django.contrib.auth.decorators import login_required

# Create your views here.
@dealer_required
@login_required
def index(request):
    return render(request,"dealer/index.html")