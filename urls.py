from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/games/', views.api_games, name='api-games'),
    path('api/games/add/', views.api_add_game, name='api-add-game'),
    path('api/games/<int:game_id>/edit/', views.api_edit_game, name='api-edit-game'),
    path('api/games/<int:game_id>/delete/', views.api_delete_game, name='api-delete-game'),
]