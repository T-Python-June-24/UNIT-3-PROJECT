from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('light/', views.light, name='light'),
    path('dark/', views.dark, name='dark'),
]