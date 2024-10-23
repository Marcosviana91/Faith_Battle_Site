from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Jogador(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avatar = models.CharField(null=True, blank=True)
    
    def __str__(self):
        return self.user.username

