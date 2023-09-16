from . import views
from django.urls import path

app_name = 'website'

urlpatterns = [
    path('',views.login,name="login"),
    path('logout',views.logout_view,name="logout")
]