from django.urls import path
from . import views
app_name = "suppliers"
urlpatterns = [
    path("all",views.all_suppliers,name="all_suppliers"),
    path("add",views.add_supplier,name="add_supplier"),
    
]