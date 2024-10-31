from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.urls import reverse

from .models import Artigo
from .forms import FormEnquetes

# Create your views here.


def site(request: HttpRequest):
    # print(request.user.id)
    return render(request, 'plataforma.html', {'player_site': 'active'})


def novidades(request: HttpRequest):
    destaques = Artigo.objects.all()  # de 3 a 5 itens
    todos_artigos = Artigo.objects.all().order_by('-data_hora_publicacao')
    ultimos_artigos = todos_artigos[:5]  # 5 itens
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
        return render(request, "novo_artigo.html", {
            'novidades': 'active',
            'logged_user': request.user,
        })
    elif request.method == "POST":
        form = request.POST
        img_capa = request.FILES['img_capa']
        novo_artigo = Artigo(
            destaque=False,
            titulo=form['titulo'],
            img_capa=img_capa,
            autor=request.user,
            conteudo=form['conteudo'],
            tag_version=form['tag_version']
        )
        novo_artigo.save()
        return HttpResponseRedirect(reverse('artigo', args=[novo_artigo.id]))


@login_required(login_url="/users/login")
def editar_artigo(request: HttpRequest, id: int):
    if request.method == "GET":
        artigo = Artigo.objects.get(id=id)
        if (artigo.autor != request.user):
            return HttpResponseRedirect(reverse('artigo', args=[id]))

        return render(request, "editar_artigo.html", {
            'novidades': 'active',
            'logged_user': request.user,
            'artigo': artigo,
        })
    elif request.method == "POST":
        form = request.POST
        artigo = Artigo.objects.get(id=id)
        artigo.titulo = form['titulo']
        artigo.conteudo = form['conteudo']
        artigo.tag_version = form['tag_version']

        artigo.save()
        return HttpResponseRedirect(reverse('artigo', args=[artigo.id]))


def artigo(request: HttpRequest, id: int):
    artigo = Artigo.objects.get(id=id)

    artigo_anterior = Artigo.objects.filter(id__lt=id).last()
    proximo_artigo = Artigo.objects.filter(id__gt=id).first()
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
