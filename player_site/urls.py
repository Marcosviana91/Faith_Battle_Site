from django.urls import path

from . import views

urlpatterns = [
    path('', views.site, name="player_site"),
    path('alpha_1_0_1/', views.alpha_1_0_1, name="alpha_1_0_1"),
]
