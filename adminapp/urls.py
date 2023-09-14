from . import views
from django.urls import path

app_name = 'adminapp'

urlpatterns = [
    path('index',views.index,name="index")
]