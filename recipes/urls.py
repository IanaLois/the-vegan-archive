from . import views
from django.urls import path


urlpatterns = [
    path("", views.RecipeList.as_view(), name="home"),
    path("recipes/", views.RecipeDirectoryView.as_view(), name="recipe_directory"),
]
