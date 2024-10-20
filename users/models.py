import os

from django.contrib.auth.models import User
from django.db import models

from faith_battle_site.settings import MEDIA_ROOT

# Create your models here.


class Jogador(User):
    avatar = models.IntegerField(default=1, null=True, blank=True)
    img_profile = models.ImageField(
        upload_to="profiles", null=True, blank=True)
