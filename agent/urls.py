from django.urls import path
from . import views


app_name = 'agent'

urlpatterns = [

    path("index",views.index,name='index'),

]
