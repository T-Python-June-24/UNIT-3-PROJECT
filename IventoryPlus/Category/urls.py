from django.urls import path
from . import views

app_name = "Category"

urlpatterns = [
    path('', views.views_Category, name="views_Category"),
    path('Category/add' , views.add_category , name='add_category'),
]