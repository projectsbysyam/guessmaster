from django.shortcuts import render

# Create your views here.

@login_required
def index(request):
    return render(request,'adminapp/index.html')

