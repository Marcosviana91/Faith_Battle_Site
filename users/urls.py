from django.urls import path

from . import views

urlpatterns = [
    path('', views.perfil, name="perfil"),
    path('cadastro/', views.cadastro, name="cadastro"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('minhas_imagens/', views.getImages, name="minhas_imagens"),
    path('meus_artigos/', views.getArticles, name="meus_artigos"),
    path('meus_jogos/', views.getGames, name="meus_jogos"),
]
