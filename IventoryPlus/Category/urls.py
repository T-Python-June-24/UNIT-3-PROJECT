from django.urls import path
from . import views

app_name = "Category"

urlpatterns = [
    path('', views.views_Category, name="views_Category"),
]