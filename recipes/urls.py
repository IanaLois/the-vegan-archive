from . import views
from django.urls import path

app_name = 'recipes'

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
]
