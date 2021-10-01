from django.urls import path, include
from . import views

app_name = 'info'

urlpatterns = [
    path('', views.home, name="home"),
    path('search_player', views.search_player, name="search_player"),
    path('player_detail', views.player_detail, name="get_player_detail"),
]