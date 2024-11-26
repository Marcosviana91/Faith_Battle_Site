from django.shortcuts import render
from django.urls import reverse
from django.http import HttpRequest, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.clickjacking import xframe_options_exempt, xframe_options_sameorigin

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

@xframe_options_sameorigin
@login_required(login_url="/users/login")
def editarJogo(request: HttpRequest, game_id: int):
    if request.method == "GET":
        game = Game.objects.get(id=game_id)
        gameBoards = GameBoard.objects.filter(game=game)
        cardFamily = CardFamily.objects.filter(game=game)
        print(cardFamily[0].deck_position_X)
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
        gameboard = GameBoard(
            name=name,
            game=game,
            image=image,
        )
        gameboard.save()
        return HttpResponseRedirect(reverse('editar_jogo', args=[game.id]))

@login_required(login_url="/users/login")
def novoDeck(request: HttpRequest):
    if request.method == "GET":
        return HttpResponseRedirect(reverse('novo_jogo'))
    elif request.method == "POST":
        title = request.POST.get("title")
        game = Game.objects.get(id=request.POST.get("game"))
        card_back_image = request.FILES.get('card_back_image')
        short_description = request.POST.get('short_description')
        top_left_txt = request.POST.get('top_left_txt')
        top_right_txt = request.POST.get('top_right_txt')
        bottom_left_txt = request.POST.get('bottom_left_txt')
        bottom_right_txt = request.POST.get('bottom_right_txt')
        if CardFamily.objects.filter(game=game).filter(title=title).exists():
            print('nome já existente para este jogo')
            return HttpResponseRedirect(reverse('editar_jogo', args=[game.id]))
        card_family = CardFamily(
            title=title,
            game=game,
            card_back_image=card_back_image,
            short_description=short_description,
            top_left_txt=top_left_txt,
            top_right_txt=top_right_txt,
            bottom_left_txt=bottom_left_txt,
            bottom_right_txt=bottom_right_txt,
            deck_position_X=0,
            deck_position_Y=0
        )
        card_family.save()
        return HttpResponseRedirect(reverse('editar_jogo', args=[game.id]))

@login_required(login_url="/users/login")
def deckPosition(request: HttpRequest):
    card_family = CardFamily.objects.get(id=request.POST.get('deck_id'))
    card_family.deck_position_X = request.POST.get('card_left')
    card_family.deck_position_Y = request.POST.get('card_bottom')
    card_family.save()
    return JsonResponse({})


# Thanks https://stackoverflow.com/questions/46080433/why-cant-django-sites-be-embedded-inside-another-htmliframe
@xframe_options_exempt
def editarCartas(request: HttpRequest, game_family_id:int):
    cardFamily = CardFamily.objects.get(id=game_family_id)
    cards = Card.objects.filter(card_family=cardFamily)
    return render(request, "editar_cartas.html", {
        'cardFamily':cardFamily,
        'cards': cards,
    })