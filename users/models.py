from django.contrib.auth.models import User
from django.db import models

from utils.files import getAvatarFileList

# Create your models here.


def getAvatarChoices():
    avatar_list = getAvatarFileList(True)
    return {i: i.split('.')[0] for i in avatar_list}


class Jogador(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.CharField(null=True, blank=True, choices=getAvatarChoices)

    def __str__(self):
        return self.user.username
