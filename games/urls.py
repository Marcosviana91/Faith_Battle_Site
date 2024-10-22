from django.urls import path

from . import views

urlpatterns = [
    # path('', views.todosJogos, name="todos_jogos"),
    # path('<int:id>', views.jogoDetalhe, name="jogo_detalhe"),
    path('novo', views.novoJogo, name="novo_jogo"),
    path('editar/<int:game_id>', views.editarJogo, name="editar_jogo"),
    path('novo_playmat', views.novoGameBoard, name="novo_playmat"),
]