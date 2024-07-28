from django.urls import path
from . import views

urlpatterns = [
    path('', views.supplier_list, name='supplier_list'),
    path('<int:pk>/', views.supplier_detail, name='supplier_detail'),
    path('add/', views.supplier_add, name='supplier_add'),
    path('<int:pk>/edit/', views.supplier_edit, name='supplier_edit'),
    path('<int:pk>/delete/', views.supplier_delete, name='supplier_delete'),
]
