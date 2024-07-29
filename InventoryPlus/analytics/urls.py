from django.urls import path
from . import views



app_name = 'analytics'


urlpatterns = [
    path('inventory-report/', views.inventory_report, name='inventory_report'),
    path('supplier-report/', views.supplier_report, name='supplier_report'),
]