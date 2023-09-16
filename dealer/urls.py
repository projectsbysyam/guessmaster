from django.urls import path
from . import views


app_name = 'dealer'

urlpatterns = [
    path("index",views.index,name='index'),
]