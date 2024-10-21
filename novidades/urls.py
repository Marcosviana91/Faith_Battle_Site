from django.urls import path

from . import views

urlpatterns = [
    path('', views.site, name="player_site"),
    path('novidades/', views.novidades, name="novidades"),
    path('artigo/novo', views.novo_artigo, name="novo_artigo"),
    path('artigo/<int:id>', views.artigo, name="artigo"),
    path('enquete/nova', views.nova_enquete, name="nova_enquete"),
]
