from django.urls import path

from . import views

urlpatterns = [
    # path('', views.todosJogos, name="todos_jogos"),
    # path('<int:id>', views.jogoDetalhe, name="jogo_detalhe"),
    path('novo', views.novoJogo, name="novo_jogo"),
    path('editar/<int:game_id>', views.editarJogo, name="editar_jogo"),
    path('editar_cartas/<int:game_family_id>', views.editarCartas, name="editar_cartas"),
    path('nova_carta/<int:deck_id>', views.criarCarta, name="nova_carta"),
    path('novo_playmat', views.novoGameBoard, name="novo_playmat"),
    path('novo_deck', views.novoDeck, name="novo_deck"),
    path('deck_position', views.deckPosition, name="deck_position"),
]