from django.urls import path
from . import views

app_name = "product"

urlpatterns = [
    path("", views.views_product, name="views_product"),
]