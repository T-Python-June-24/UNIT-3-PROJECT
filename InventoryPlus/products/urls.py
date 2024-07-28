from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path("add/", views.add_product_view, name="add_product_view"),
    path("search/", views.search_products_view, name="search_products_view"),
    path("<category_name>/", views.all_products_view, name="all_products_view"),

]