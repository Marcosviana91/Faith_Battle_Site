import os

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login as login_user, logout as logout_user
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from faith_battle_site.settings import MEDIA_ROOT
from .forms import UploadFileForm
from novidades.models import Artigo


MAX_DIR_SIZE_IM_MB = 2

# Create your views here.


def cadastro(request: HttpRequest):
    if request.method == "GET":
        return render(request, "cadastro.html")
    username = request.POST.get("username")

    user = User.objects.filter(username=username).first()
    if user:
        return HttpResponse("Ja cadastrado")
    email = request.POST.get("email")
    password = request.POST.get("password")
    user = User.objects.create_user(username, email, password)
    # user.is_active = False
    user.save()
    return HttpResponse(f'{username} {email} {password}')


def login(request: HttpRequest):
    if request.method == 'GET':
        return render(request, "login.html")
    username = request.POST.get("username")
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
    print(request.user.is_authenticated)
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    logged_user = User.objects.get(username=request.user)
    return render(request, "logged_area.html", {
        'perfil': 'active',
        'logged_user': request.user,
    })

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

    user_dir_size = 0
    all_images = os.listdir(user_media_dir)
    for img in all_images:
        img_size = os.path.getsize(os.path.join(user_media_dir, img))
        user_dir_size += img_size
    user_dir_size = (user_dir_size/1024/1024)
    print(f'{round(user_dir_size, 2)}/{MAX_DIR_SIZE_IM_MB} MB')

    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if user_dir_size > MAX_DIR_SIZE_IM_MB:
            return render(request, "minhas_imagens.html", {
                'all_images': all_images,
                'user_media_url': user_media_url,
                'form': form,
                'logged_user': request.user,
            })
        if form.is_valid():
            imagem = form.files['imagem']
            destination_file = os.path.join(user_media_dir, imagem.name)
            with open(destination_file, "wb") as destination:
                for chunk in imagem.chunks():
                    destination.write(chunk)

    else:
        form = UploadFileForm()

    return render(request, "minhas_imagens.html", {
        'all_images': all_images,
        'user_media_url': user_media_url,
        'form': form,
        'logged_user': request.user,
    })


@login_required(login_url="/users/login")
def getArticles(request: HttpRequest):
    meus_artigos = Artigo.objects.filter(autor=request.user)
    print(meus_artigos)
    return render(request, "meus_artigos.html", {
        'my_articles': meus_artigos,
        'logged_user': request.user,
    })
