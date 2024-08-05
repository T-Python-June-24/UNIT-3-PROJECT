from django.urls import path
from . import views


app_name = "inventory"

urlpatterns = [
    path("", views.plotly_view, name="home_view"),
    path("inventory/", views.inventory, name="inventory_view"),
    path("update/<int:product_id>/", views.stock_update, name="stock_update"),

]