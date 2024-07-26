from django.urls import path
from . import views


app_name = "Supplier"

urlpatterns = [
    path('add/',views.add_supplier,name="add_supplier"),
    path('add-succses/',views.added_success,name="added_success"),
    path('detail/<supplier_id>/',views.supplier_detail,name="supplier_detail"),
    path("all-suppliers/", views.supplier_page, name="supplier_page"),
    path('update/<supplier_id>/', views.supplier_update, name='supplier_update'),    
    path("delete/<supplier_id>/", views.delete_supplier, name="delete_supplier"),

]