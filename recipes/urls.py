from django.urls import path
from . import views

urlpatterns = [
    path("", views.RecipeList.as_view(), name="home"),
    path("recipes/", views.RecipeDirectoryView.as_view(), name="recipe_directory"),
    path('recipe/<int:id>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('recipe/<int:id>/like/', views.RecipeLike.as_view(), name='recipe_like'),
    path('recipe/create/', views.RecipeCreate.as_view(), name='recipe_create'),
    path('recipe/<int:id>/update/', views.RecipeUpdate.as_view(), name='recipe_update'),
    path('recipe/<int:id>/delete/', views.RecipeDelete.as_view(), name='recipe_delete'),
]