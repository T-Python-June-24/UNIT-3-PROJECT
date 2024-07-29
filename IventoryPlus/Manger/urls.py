from django.urls import path
from . import views

app_name = "Manger"

urlpatterns = [
    path("", views.Manger, name="Manger"),
    path("views/product" , views.manger_product , name="manger_product"),
    path("views/Category" , views.manger_Category , name="manger_Category"),
    
]