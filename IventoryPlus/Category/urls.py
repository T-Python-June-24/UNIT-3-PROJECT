from django.urls import path
from . import views


app_name = "Category"

urlpatterns = [
    path("add/", views.add_category, name="add_category"),
    path("categories/", views.category_page, name="category_page"),
    path('added-success/', views.category_added_success, name='category_added_success'),
    path('detail/<category_id>/', views.category_detail, name='category_detail'),    
    
    path('update/<category_id>/', views.category_update, name='category_update'),    
    path("delete/<category_id>/", views.delete_category, name="delete_category"),

    # path("update/<game_id>/", views.game_update_view, name="game_update_view"),
    # path("search/", views.search_games_view, name="search_games_view"),
    # path("<category_name>/", views.all_games_view, name="all_games_view"),
    # path("reviews/add/<game_id>/", views.add_review_view, name="add_review_view")
]