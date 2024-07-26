from django.urls import path
from . import views

app_name = "mian"

urlpatterns = [
    path("", views.home, name="home"),
]