from django.db import models


# Create your models here.

class CardSession(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.name


class Card(models.Model):
    id = models.AutoField(primary_key=True)
    is_active = models.BooleanField(default=True)
    session = models.ForeignKey(
        CardSession, on_delete=models.CASCADE, default=None)
    slug = models.CharField(max_length=30, unique=True, db_index=True)
    wisdom_cost = models.IntegerField(default=0)
    attack_point = models.IntegerField(default=0)
    defense_points = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.slug
    
