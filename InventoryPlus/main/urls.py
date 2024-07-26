from django.urls import path
from . import views

appname = "main"

urlpatterns = [
    path('', views.home_view, name='home_view'),
]