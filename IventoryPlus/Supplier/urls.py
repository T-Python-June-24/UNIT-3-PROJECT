from django.urls import path
from . import views

app_name = "Supplier"

urlpatterns = [
    path("", views.views_supplier, name="views_supplier"),
]