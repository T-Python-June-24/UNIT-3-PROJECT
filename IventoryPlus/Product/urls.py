from django.urls import path
from . import views


app_name = "Product"

urlpatterns = [
    path('add/',views.add_product,name="add_product"),
    path('add-succses/',views.Product_added_success,name="Product_added_success"),
    path('all/',views.product_page,name="product_page"),
    path('detail/<product_id>/', views.product_detail, name='product_detail'),    
    path('update/<product_id>/', views.product_update, name='product_update'),    

    
]