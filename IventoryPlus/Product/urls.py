from django.urls import path
from . import views


app_name = "Product"

urlpatterns = [
    path('add/',views.add_product,name="add_product"),
    path('add-succses/',views.Product_added_success,name="Product_added_success"),
]