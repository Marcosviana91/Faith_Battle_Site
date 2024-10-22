from django.shortcuts import render
from django.urls import reverse
from django.http import HttpRequest, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.clickjacking import xframe_options_exempt

from .models import Game, GameBoard, CardFamily, Card

# Create your views here.


@login_required(login_url="/users/login")
def novoJogo(request: HttpRequest):
    if request.method == "GET":
        return render(request, "novo_jogo.html", {
            'logged_user': request.user,
        })
    elif request.method == "POST":
        created_by = request.user
        title = request.POST.get("title")
        description = request.POST.get("description")
        image = request.FILES.get('image')
        # print(image)
        game = Game(
            created_by=created_by,
            title=title,
            description=description,
            image=image,
        )
        game.save()
        return HttpResponseRedirect(reverse('editar_jogo', args=[game.id]))


@login_required(login_url="/users/login")
def editarJogo(request: HttpRequest, game_id: int):
    if request.method == "GET":
        game = Game.objects.get(id=game_id)
        gameBoards = GameBoard.objects.filter(game=game)
        cardFamily = CardFamily.objects.filter(game=game)
        print(gameBoards)
        return render(request, "editar_jogo.html", {
            'logged_user': request.user,
            'game': game,
            'gameboards': gameBoards,
            'cardfamily': cardFamily,
        })
    elif request.method == "POST":
        created_by = request.user
        title = request.POST.get("title")
        description = request.POST.get("description")
        image = request.FILES.get('image')
        print(image)
        game = Game(
            created_by=created_by,
            title=title,
            description=description,
            image=image,
        )
        # game.save()
        return render(request, "editar_jogo.html", {
            'logged_user': request.user,
            'game': game,
        })
        # return HttpResponseRedirect(reverse('editar_jogo', args=[game_id]))


@login_required(login_url="/users/login")
def novoGameBoard(request: HttpRequest):
    if request.method == "GET":
        return HttpResponseRedirect(reverse('novo_jogo'))
    elif request.method == "POST":
        name = request.POST.get("name")
        game = Game.objects.get(id=request.POST.get("game"))
        image = request.FILES.get('image')
        # print(image)
        gameboard = GameBoard(
            name=name,
            game=game,
            image=image,
        )
        gameboard.save()
        return HttpResponseRedirect(reverse('editar_jogo', args=[game.id]))


# Thanks https://stackoverflow.com/questions/46080433/why-cant-django-sites-be-embedded-inside-another-htmliframe
@xframe_options_exempt
def verCartas(request: HttpRequest, game_family_id:int):
    cardFamily = CardFamily.objects.get(id=game_family_id)
    cards = Card.objects.filter(card_family=cardFamily)
    print(cards)
    return render(request, "ver_cartas.html", {
        'cardFamily':cardFamily,
        'cards': cards,
    })