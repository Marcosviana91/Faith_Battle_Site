from django.db import models
from .choices import ChoicesTipoCarta, ChoicesSession

# Create your models here.


class Game(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(default='')
    image = models.ImageField(upload_to="games", null=True, blank=True)

    def __str__(self):
        return self.title


# class GameBoard(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=30, unique=True, db_index=True)
#     image = models.ImageField(upload_to="game_boards", null=True, blank=True)
#     game = models.ForeignKey(Game, null=True, on_delete=models.CASCADE)

#     def __str__(self) -> str:
#         return self.name


# class CardFamily(models.Model):
#     id = models.AutoField(primary_key=True)
#     game = models.ForeignKey(
#         Game, null=True, blank=False, on_delete=models.CASCADE)
#     title = models.CharField(max_length=255, blank=False, null=False)
#     description = models.TextField(default='')
#     card_back_image = models.ImageField(
#         upload_to="cards", null=True, blank=True)

#     def __str__(self):
#         return self.title


class Card(models.Model):
    id = models.AutoField(primary_key=True)
    # card_family = models.ForeignKey(
        # CardFamily, null=True, blank=False, on_delete=models.CASCADE)

    is_active = models.BooleanField(default=True)
    card_type = models.CharField(
        max_length=25, choices=ChoicesTipoCarta, default="hero")
    card_image = models.ImageField(upload_to="cards", null=True, blank=True)
    card_image_mini = models.ImageField(
        upload_to="cards", null=True, blank=True)
    card_description = models.CharField(max_length=250, default='')
    session = models.CharField(max_length=25, choices=ChoicesSession)
    slug = models.CharField(max_length=30, unique=True, db_index=True)
    wisdom_cost = models.IntegerField(default=0)
    attack_point = models.IntegerField(default=0)
    defense_points = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.slug
