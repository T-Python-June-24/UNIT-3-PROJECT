from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('add/', views.add, name='add'),

]
