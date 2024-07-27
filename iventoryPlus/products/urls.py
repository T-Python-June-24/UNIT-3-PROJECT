from django.urls import path
from . import views
app_name = "products"
urlpatterns = [
    path("all/",views.products_view,name="products_view"),
    path("add/",views.add_product_view,name="add_product_view"),

]