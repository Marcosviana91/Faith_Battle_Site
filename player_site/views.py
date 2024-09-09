from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
@login_required(login_url="/users/login")
def site(request: HttpRequest):
    return render(request, 'plataforma.html')
