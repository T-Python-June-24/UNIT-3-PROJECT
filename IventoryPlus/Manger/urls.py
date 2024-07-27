from django.urls import path
from . import views

app_name = "Manger"

urlpatterns = [
    path("", views.Manger, name="Manger"),
]