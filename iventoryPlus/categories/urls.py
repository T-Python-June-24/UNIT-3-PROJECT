from django.urls import path
from . import views
app_name = "categories"
urlpatterns = [    
path('all/',views.all_categories,name="all_categories"),
path("add/",views.add_category,name="add_category"),

]