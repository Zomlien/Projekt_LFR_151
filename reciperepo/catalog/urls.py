from django.urls import path
from . import views

# app_name ='recipe'

urlpatterns = [
    path('category/', views.category_list, name='category_list'),
    # recipe Urls
    path('recipe/', views.recipe_list, name='recipe_list'),
    path('recipe/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/create/', views.recipe_create, name='recipe_create'),
    path('recipe/<int:pk>/edit', views.recipe_edit, name='recipe_edit'),
    path('recipe/delete/<int:pk>/', views.recipe_delete, name='recipe_delete'),
    # Home Url
    path('', views.home, name='home'),
]
