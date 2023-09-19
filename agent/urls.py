from django.urls import path
from . import views

app_name = 'agent'

urlpatterns = [
    path("index",views.index,name='index'),
    path('add_dealer',views.add_dealer,name="add_dealer"), 
    path('view_dealer',views.view_dealer,name="view_dealer"),
]
