from . import views
from django.urls import path

app_name = 'adminapp'

urlpatterns = [
    path('index',views.index,name="index"),
    path('agent',views.agent,name="agent"),
    path('add-agent',views.add_agent,name="add_agent"),
    path('dealer',views.dealer,name="dealer"),
    path('change-game',views.change_game,name="changegame"),
]