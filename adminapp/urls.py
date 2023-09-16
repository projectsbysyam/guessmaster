from . import views
from django.urls import path

app_name = 'adminapp'

urlpatterns = [
    path('index',views.index,name="index"),
    path('agent',views.agent,name="agent"),
    path('addagent',views.addagent,name="addagent"),
    path('dealer',views.dealer,name="dealer"),
    path('changegame',views.changegame,name="changegame"),


]