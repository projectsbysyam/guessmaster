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
    path('edit-package/<int:id>',views.edit_package,name="edit_package"),
    path('delete-package/<int:id>',views.delete_package,name="delete_package"),
    path('add-result',views.add_result,name="add_result"),
    path('view-results',views.results,name="view_results"),
    path('sales-report',views.sales_report,name="sales_report"),
    path('add-time',views.add_time,name="add_time"),
    path('change-time',views.change_time,name="change_time"),
    path('change-game-time/<int:id>',views.change_game_time,name="change_game_time"),
    path('monitor',views.monitor,name="monitor"),
    path('dailyreport',views.daily_report,name="dailyreport"),
    path('countwise-report',views.countwise_report,name="countwise_report"),
    path('countsales-report',views.countsales_report,name="countsales_report"),
    path('winning_report',views.winning_report,name="winning_report"),
    path('winningcount-report',views.winningcount_report,name="winningcount_report"),
    path('blocked_numbers',views.blocked_numbers,name="blocked_numbers"),
    path('edit_bill',views.edit_bill,name="edit_bill"),
    path('payment_report',views.payment_report,name="payment_report"),
    path('change_password',views.change_password,name="change_password"),
    path('settings',views.settings,name="settings"),



    


]