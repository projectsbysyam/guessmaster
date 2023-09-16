from django.urls import path
from . import views


app_name = 'dealer'

urlpatterns = [

    path("",views.index,name='index'),



]