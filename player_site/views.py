from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render

# Create your views here.
# @login_required(login_url="/users/login")
def site(request: HttpRequest):
    # print(request.user.id)
    return render(request, 'plataforma.html')

def alpha_1_0_1(request: HttpRequest):
    return render(request, 'versions/alpha_1.0.1.html')
