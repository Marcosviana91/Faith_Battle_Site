from django.urls import path

from . import views

urlpatterns = [
    path('', views.site, name="player_site"),
]
