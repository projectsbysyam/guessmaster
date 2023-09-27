from django.urls import path
from . import views

app_name = 'agent'

urlpatterns = [
    path("index",views.index,name='index'),
    path('add-dealer',views.add_dealer,name="add_dealer"), 
    path('view-dealer',views.view_dealer,name="view_dealer"),
    path('ban-dealer/<int:id>',views.ban_dealer,name="ban_dealer"),
    path('remove-ban/<int:id>',views.remove_ban,name="remove_ban"),
    path('remove-ban/<int:id>',views.remove_ban,name="remove_ban"),
    path('delete-dealer/<int:id>',views.delete_dealer,name="delete_dealer"),
    path('edit-dealer/<int:id>',views.edit_dealer,name="edit_dealer"),
    path('Results',views.results,name="results"),

    path('booking',views.booking,name="booking"), 
    path('sales-report',views.sales_report,name="sales_report"), 
    path('daily-report',views.daily_report,name="daily_report"), 
    path('winning-report',views.winning_report,name="winning_report"),
    path('count-salesreport',views.count_salereport,name="count_salereport"),
    path('winning_countreport',views.winning_countreport,name="winning_countreport"),
    path('collection-report',views.collection_report,name="collection_report"),
    path('add-collection',views.add_collection,name="add_collection"),
    path('balance-report',views.balance_report,name="balance_report"),
    path('edit-bill',views.edit_bill,name="edit_bill"),
    path('change-password',views.change_password,name="change_password"),

    path('play-game/<int:id>',views.play_game,name="play_game"),


    path('package',views.package,name="package"),
    path('new-package',views.new_package,name="new_package"),
    path('edit-package/<int:id>',views.edit_package,name="edit_package"),
    path('delete-package/<int:id>',views.delete_package,name="delete_package"),
]