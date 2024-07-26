from django.urls import path
from . import views

app_name = "publishers"

urlpatterns = [
    path("", views.views_product, name="views_product"),
]