from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('<int:pk>/', views.category_detail, name='category_detail'),
    path('add/', views.category_add, name='category_add'),
    path('<int:pk>/edit/', views.category_edit, name='category_edit'),
    path('<int:pk>/delete/', views.category_delete, name='category_delete'),
]
