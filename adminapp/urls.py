from . import views
from django.urls import path

app_name = 'adminapp'

urlpatterns = [
    path('index',views.index,name="index"),
    path('agent',views.agent,name="agent"),
    path('add-agent',views.add_agent,name="add_agent"),
    path('view-agent',views.view_agent,name="view_agent"),
    path('delete-agent/<int:id>',views.delete_agent,name="delete_agent"),
    path('ban-agent/<int:id>',views.ban_agent,name="ban_agent"),
    path('remove-ban/<int:id>',views.remove_ban,name="remove_ban"),
    path('package',views.package,name="package"),
    path('new-package',views.new_package,name="new_package"),
    path('create-winningprice',views.create_winningprice,name="create_winningprice"),
    path('sales-report',views.sales_report,name="sales_report"),

    path('change-game',views.change_game,name="changegame"),
    path('monitor',views.monitor,name="monitor"),
    path('results',views.results,name="results"),
    path('dailyreport',views.daily_report,name="dailyreport"),
    path('change-password',views.change_password,name="change_password"),
]