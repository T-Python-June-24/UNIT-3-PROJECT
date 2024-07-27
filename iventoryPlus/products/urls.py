from django.urls import path
from . import views
app_name = "products"
urlpatterns = [
    path("all/",views.products_view,name="products_view"),
    path("add/",views.add_product_view,name="add_product_view"),
    path("update/<product_id>",views.update_product,name="update_product"),
    path("delete/<product_id>",views.delete_product,name="delete_product")

]