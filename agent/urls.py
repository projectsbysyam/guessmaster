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
]