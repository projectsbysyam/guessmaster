from django.urls import path
from . import views


app_name = 'dealer'

urlpatterns = [

    path("index",views.index,name='index'),
    path('booking',views.booking,name="booking"), 
    path('result',views.result,name="result"), 
    path('edit-bill',views.edit_bill,name="edit_bill"),
    path('sales-report',views.sales_report,name="sales_report"), 






]