from django.urls import path

from . import views

urlpatterns = [
    path('', views.novidades, name="novidades"),
    path('artigo/<int:id>', views.artigo, name="artigo"),
    path('enquete/nova', views.nova_enquete, name="nova_enquete"),
]
