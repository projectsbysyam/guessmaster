from . import views
from django.urls import path

app_name = 'adminapp'

urlpatterns = [
    path('index',views.index,name="index"),
    path('agent',views.agent,name="agent"),
    path('add-agent',views.add_agent,name="add_agent"),
    path('view-agent',views.view_agent,name="view_agent"),
    path('edit-agent/<int:id>',views.edit_agent,name="edit_agent"),
    path('delete-agent/<int:id>',views.delete_agent,name="delete_agent"),
    path('ban-agent/<int:id>',views.ban_agent,name="ban_agent"),
    path('remove-ban/<int:id>',views.remove_ban,name="remove_ban"),
    path('package',views.package,name="package"),
    path('new-package',views.new_package,name="new_package"),
    path('create-winningprice',views.create_winningprice,name="create_winningprice"),
    path('sales-report',views.sales_report,name="sales_report"),
    path('countwise-report',views.countwise_report,name="countwise_report"),
    path('countsales-report',views.countsales_report,name="countsales_report"),
    path('winning-report',views.winning_report,name="winning_report"),
    path('winningcount_report',views.winningcount_report,name="winningcount_report"),
    path('blocked-numbers',views.blocked_numbers,name="blocked_numbers"), 
    path('change-game',views.change_game,name="changegame"),
    path('edit-bill',views.edit_bill,name="edit_bill"),
    path('monitor',views.monitor,name="monitor"),
    path('results',views.results,name="results"),
    path('dailyreport',views.daily_report,name="dailyreport"),
    path('change-password',views.change_password,name="change_password"),
    path('settings',views.settings,name="settings"),
]