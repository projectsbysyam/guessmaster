from . import views
from django.urls import path

app_name = 'adminapp'

urlpatterns = [
    path('index',views.index,name="index"),
    path('agent',views.agent,name="agent"),
    path('add-agent',views.add_agent,name="add_agent"),
    path('view-agent',views.view_agent,name="view_agent"),
    path('change-game',views.change_game,name="changegame"),
    path('monitor',views.monitor,name="monitor"),
    path('results',views.results,name="results"),
    path('dailyreport',views.daily_report,name="dailyreport"),
    path('change-password',views.change_password,name="change_password"),

]