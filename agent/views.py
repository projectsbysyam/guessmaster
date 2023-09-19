from django.shortcuts import render

# Create your views here.
def index(request):
    print(request.user)
    user = request.user
    if user.is_active:
        print("User is active")
    else:
        print("User is not active")
    return render(request,"agent/index.html")