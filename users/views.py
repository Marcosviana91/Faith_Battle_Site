from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_user


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
        return HttpResponseRedirect('/site')
    return HttpResponse('Auth invalido')
