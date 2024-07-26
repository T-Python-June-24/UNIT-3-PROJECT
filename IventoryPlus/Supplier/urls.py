from django.urls import path
from . import views


app_name = "Supplier"

urlpatterns = [

    path('add/',views.add_supplier,name="add_supplier"),
    path('add-succses/',views.added_success,name="added_success"),
]