from django.shortcuts import render
from django.urls import reverse
from django.http import HttpRequest, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.clickjacking import xframe_options_exempt, xframe_options_sameorigin

from .models import Game, GameBoard, CardFamily, Card

# Create your views here.


@login_required(login_url="/users/login")
@staff_member_required(login_url="/users/login")
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
@staff_member_required(login_url="/users/login")
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
@staff_member_required(login_url="/users/login")
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
@staff_member_required(login_url="/users/login")
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
@staff_member_required(login_url="/users/login")
def deckPosition(request: HttpRequest):
    card_family = CardFamily.objects.get(id=request.POST.get('deck_id'))
    card_family.deck_position_X = request.POST.get('card_left')
    card_family.deck_position_Y = request.POST.get('card_bottom')
    card_family.save()
    return JsonResponse({})


# Thanks https://stackoverflow.com/questions/46080433/why-cant-django-sites-be-embedded-inside-another-htmliframe
@xframe_options_exempt
@login_required(login_url="/users/login")
@staff_member_required(login_url="/users/login")
def editarCartas(request: HttpRequest, game_family_id:int):
    if request.method == "GET":
        cardFamily = CardFamily.objects.get(id=game_family_id)
        cards = Card.objects.filter(card_family=cardFamily)
        return render(request, "editar_cartas.html", {
            'cardFamily':cardFamily,
            'cards': cards,
        })
    elif request.method == "POST":
        print(request.POST)
        
@login_required(login_url="/users/login")
@staff_member_required(login_url="/users/login")
def criarCarta(request: HttpRequest, deck_id:int):
    if request.method == "GET":
        return HttpResponseRedirect(reverse('editar_cartas', args=[deck_id]))
    elif request.method == "POST":
        cardFamily = CardFamily.objects.get(id=deck_id)
        print(request.POST)
        is_active = request.POST.get('is_active')
        slug = request.POST.get('slug')
        card_description = request.POST.get('card_description')
        top_left_value = request.POST.get('top_left_value')
        top_right_value = request.POST.get('top_right_value')
        bottom_left_value = request.POST.get('bottom_left_value')
        bottom_right_value = request.POST.get('bottom_right_value')
        # FILES
        card_image = request.FILES.get('card_image')
        card_image_mini = request.FILES.get('card_image_mini')
        print(is_active=='on')
        new_card = Card(
            game=cardFamily.game,
            card_family=cardFamily,
            is_active=is_active=='on',
            slug=slug,
            card_description=card_description,
            top_left_value=top_left_value,
            top_right_value=top_right_value,
            bottom_left_value=bottom_left_value,
            bottom_right_value=bottom_right_value,
            card_image=card_image,
            card_image_mini=card_image_mini
        )
        new_card.save()
        return HttpResponseRedirect(reverse('editar_cartas', args=[deck_id]))