from django.urls import path
from . import views



app_name = 'inventory'


# urlpatterns = [
#     path('', views.product_list, name='product_list'),
#     path('product/<int:pk>/', views.product_detail, name='product_detail'),
#     path('product/new/', views.product_create, name='product_create'),
#     path('product/<int:pk>/edit/', views.product_edit, name='product_edit'),
#     path('product/<int:pk>/delete/', views.product_delete, name='product_delete'),
# ]



urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/new/', views.product_create, name='product_create'),
    path('product/<int:pk>/edit/', views.product_update, name='product_update'),
    path('product/<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('suppliers/', views.supplier_list, name='supplier_list'),
    path('supplier/<int:pk>/', views.supplier_detail, name='supplier_detail'),
    path('supplier/new/', views.supplier_create, name='supplier_create'),
    path('supplier/<int:pk>/edit/', views.supplier_edit, name='supplier_edit'),
    path('supplier/<int:pk>/delete/', views.supplier_delete, name='supplier_delete'),
    path('categories/', views.category_list, name='category_list'),
    path('category/new/', views.category_create, name='category_create'),
    path('category/<int:pk>/edit/', views.category_edit, name='category_edit'),
    path('category/<int:pk>/delete/', views.category_delete, name='category_delete'),
    path('export/', views.export_products_csv, name='export_products_csv'),
    path('import/', views.import_products_csv, name='import_products_csv'),
    path('search/', views.search, name='search'),
]

