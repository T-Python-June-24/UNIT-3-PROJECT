from django.urls import path
from . import views


app_name = "suppliers"

urlpatterns = [
    path("add/", views.add_supplier, name="add_supplier"),
    path("all/", views.all_suppliers, name="all_suppliers"),
    # path("update/<supplier_id>/", views.game_update_view, name="game_update_view"),
    # path("delete/<supplier_id>/", views.game_delete_view, name="game_delete_view"),
    # path("search/", views.search_games_view, name="search_games_view"),
    # path("<category_name>/", views.all_games_view, name="all_games_view"),
    # path("reviews/add/<game_id>/", views.add_review_view, name="add_review_view")
]