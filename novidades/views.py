
# from urllib.parse import quote

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpRequest

from .models import Artigo
from .forms import FormEnquetes, FormArtigos

# Create your views here.


def site(request: HttpRequest):
    # print(request.user.id)
    return render(request, 'plataforma.html', {'player_site': 'active'})


def novidades(request: HttpRequest):
    destaques = Artigo.objects.all() # de 3 a 7 itens
    todos_artigos = Artigo.objects.all().order_by('-data_hora_publicacao')
    ultimos_artigos = todos_artigos[:5] # 5 itens
    # print(destaques)
    return render(request, "novidades.html", {
        'destaques': destaques,
        'novidades': 'active',
        'ultimos_artigos': ultimos_artigos,
        'todos_artigos': todos_artigos,
    })


@login_required(login_url="/users/login")
def novo_artigo(request: HttpRequest):
    if request.method == "GET":
        form = FormArtigos()
        return render(request, "novo_artigo.html", {
            'novidades': 'active',
            'logged_user': request.user,
            'form': form
        })
    elif request.method == "POST":
        form = FormEnquetes(request.POST)
        if form.is_valid():
            form
            form.save()
            return render(request, "novo_artigo.html", {
                'novidades': 'active',
                'logged_user': request.user,
                'form': form
            })
        else:
            return render(request, "novo_artigo.html", {
                'novidades': 'active',
                'logged_user': request.user,
                'form': form
            })


def artigo(request: HttpRequest, id: int):
    artigo = Artigo.objects.get(id=id)
    artigo_anterior = Artigo.objects.filter(id=id-1).first()
    proximo_artigo = Artigo.objects.filter(id=id+1).first()
    return render(request, "artigo.html", {
        'novidades': 'active',
        'artigo': artigo,
        'artigo_anterior': artigo_anterior,
        'proximo_artigo': proximo_artigo,
        'logged_user': request.user,
    })


@login_required(login_url="/users/login")
def nova_enquete(request: HttpRequest):
    if request.method == "GET":
        form = FormEnquetes()
        return render(request, "enquete.html", {'form': form})
    elif request.method == "POST":
        form = FormEnquetes(request.POST)
        if form.is_valid():
            form
            form.save()
            return render(request, "novo_servico.html", {'form': form})
        else:
            return render(request, "novo_servico.html", {'form': form})
