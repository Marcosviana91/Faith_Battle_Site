import os
import json

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login as login_user, logout as logout_user
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from faith_battle_site.settings import MEDIA_ROOT
from .forms import UploadFileForm
from .models import Jogador
from novidades.models import Artigo
from games.models import Game

from utils.files import getAvatarFileList

MAX_DIR_SIZE_IM_MB = 200

# Create your views here.


def cadastro(request: HttpRequest):
    if request.method == "GET":
        return HttpResponseRedirect(reverse('login')+'?form_tab=cadastrar')
        # return render(request, "cadastro.html")
    if request.method == "POST":
        form = request.POST
        username = form.get("username").lower()

        user = User.objects.filter(username=username).first()
        if user:
            return HttpResponse("Já tem um username cadastrado")
        password = form.get("password")
        first_name = form.get("first_name")
        user = User.objects.create_user(
            username=username, password=password, first_name=first_name)
        user.save()

        avatar = form.get("avatar")
        novo_jogador = Jogador(user=user, avatar=avatar)
        novo_jogador.save()
        return HttpResponseRedirect(reverse('login'))
    return HttpResponse(f"Metodo {request.method} não implementado....")


def login(request: HttpRequest):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('perfil'))
        return render(request, "login.html", {'all_avatar': getAvatarFileList()})

    username = request.POST.get("username").lower()
    password = request.POST.get("password")

    user = authenticate(username=username, password=password)
    if user:
        login_user(request, user)
        return HttpResponseRedirect(reverse('perfil'))
    return HttpResponse('Auth invalido')


def logout(request: HttpRequest):
    logout_user(request)
    return HttpResponseRedirect(reverse('login'))


# Verificação de usuário manual
def perfil(request: HttpRequest):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    player_data = Jogador.objects.get(user=request.user)
    if request.method == "GET":
        return render(request, "logged_area.html", {
            'perfil': 'active',
            'logged_user': request.user,
            'player_data': player_data
        })
    elif request.method == "POST":
        form = request.POST
        user = User.objects.get(username=request.user.username)
        user.first_name = form.get("first_name")
        user.email = form.get("email")
        player_data.avatar = form.get("avatar")
        user.save()
        player_data.save()

        # TODO: implementar mensagem de dados salvo com sucesso
        return render(request, "logged_area.html", {
            'perfil': 'active',
            'logged_user': user,
            'player_data': player_data
        })
    return HttpResponse(f"Metodo {request.method} não implementado....")


# Decorador de verificação de usuário
@login_required(login_url="/users/login")
def getImages(request: HttpRequest):
    user_id = str(request.user.id)
    user_path = os.path.join(
        MEDIA_ROOT,
        'users_images',
        user_id
    )
    if not os.path.exists(user_path):
        os.makedirs(user_path)

    user_media_dir = os.path.join(MEDIA_ROOT, "users_images", user_id)
    user_media_url = os.path.join(os.path.basename(
        MEDIA_ROOT), "users_images", user_id)

    all_images = sorted(os.listdir(user_media_dir))
    user_dir_size = 0
    for img in all_images:
        img_size = os.path.getsize(os.path.join(user_media_dir, img))
        user_dir_size += img_size
    user_dir_size = round(user_dir_size/1024/1024, 2)
    print(f'{user_dir_size}/{MAX_DIR_SIZE_IM_MB} MB')

    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if user_dir_size > MAX_DIR_SIZE_IM_MB:
            return render(request, "minhas_imagens.html", {
                'all_images': all_images,
                'user_media_url': user_media_url,
                'form': form,
                'logged_user': request.user,
                'MAX_DIR_SIZE_IM_MB': MAX_DIR_SIZE_IM_MB,
                'user_dir_size': user_dir_size
            })
        if form.is_valid():
            imagem = form.files['imagem']
            destination_file = os.path.join(user_media_dir, imagem.name)
            with open(destination_file, "wb") as destination:
                for chunk in imagem.chunks():
                    destination.write(chunk)

    else:
        file_to_delete = request.GET.get('del')
        if file_to_delete:
            print(f"Apagar {file_to_delete}")
            os.remove(os.path.join(user_path,file_to_delete))
            return HttpResponseRedirect(reverse('minhas_imagens'))
        form = UploadFileForm()
    all_images = os.listdir(user_media_dir)
    images_info = []
    
    user_dir_size = 0
    for img in all_images:
        img_size = os.path.getsize(os.path.join(user_media_dir, img))
        images_info.append({
            'name':img,
            'size': round(img_size/1024/1024, 2) # in MB
        })
        user_dir_size += img_size
    user_dir_size = round(user_dir_size/1024/1024,2)
    return render(request, "minhas_imagens.html", {
        'all_images':all_images,
        'images_info':json.dumps(images_info),
        'user_media_url': user_media_url,
        'form': form,
        'logged_user': request.user,
        'MAX_DIR_SIZE_IM_MB': MAX_DIR_SIZE_IM_MB,
        'user_dir_size': user_dir_size
    })


@login_required(login_url="/users/login")
def getArticles(request: HttpRequest):
    meus_artigos = Artigo.objects.filter(autor=request.user)
    print(meus_artigos)
    return render(request, "meus_artigos.html", {
        'my_articles': meus_artigos,
        'logged_user': request.user,
    })


@login_required(login_url="/users/login")
def getGames(request: HttpRequest):
    meus_jogos = Game.objects.filter(created_by=request.user)
    print(meus_jogos)
    return render(request, "meus_jogos.html", {
        'meus_jogos': meus_jogos,
        'logged_user': request.user,
    })
