from . import views
from django.urls import path


app_name = 'Product'

urlpatterns = [
    path('', views.home, name='home')
]
