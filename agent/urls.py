from django.urls import path
from . import views


app_name = 'agent'

urlpatterns = [

path("",views.index,name='index'),

]
