from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Game(models.Model):
    id = models.AutoField(primary_key=True)
    created_by = models.ForeignKey(
        User, null=True, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(default='')
    image = models.ImageField(upload_to="games", null=True, blank=True)
    # packageTimeStamp = models.CharField(max_length=150)

    def __str__(self):
        return self.title

    def save(self):
        img_file_type = self.image.name.split(".")[-1]
        self.image.name = f'{self.title.lower().replace(" ", "_")}.{
            img_file_type}'
        super().save()


class GameBoard(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, db_index=True)
    game = models.ForeignKey(Game, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="game_boards", null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    def save(self):
        img_file_type = self.image.name[-3:]
        self.image.name = f'{self.game.title.lower().replace(" ", "_")}_{self.name.lower().replace(" ", "_")}.{
            img_file_type}'
        super().save()


class CardFamily(models.Model):
    id = models.AutoField(primary_key=True)
    game = models.ForeignKey(
        Game, null=True, blank=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, blank=False, null=False)
    short_description = models.CharField(
        max_length=255, blank=False, null=False)
    card_back_image = models.ImageField(
        null=True, blank=True)

    top_left_txt = models.CharField(
        max_length=30, default='', blank=True, null=True)
    top_right_txt = models.CharField(
        max_length=30, default='', blank=True, null=True)
    bottom_left_txt = models.CharField(
        max_length=30, default='', blank=True, null=True)
    bottom_right_txt = models.CharField(
        max_length=30, default='', blank=True, null=True)

    deck_position_X = models.IntegerField(blank=True, null=True)
    deck_position_Y = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self):
        img_file_type = self.card_back_image.name[-3:]
        self.card_back_image.name = f'cards/{self.game.title.lower().replace(" ", "_")}_{self.title.lower().replace(" ", "_")}.{
            img_file_type}'
        # self.card_back_image.url.split("/")[2]
        super().save()


def getCardFamilyByGame(game):
    card_family_list = CardFamily.objects.filter(game=game)
    return {i: i.split('.')[0] for i in card_family_list}


class Card(models.Model):
    id = models.AutoField(primary_key=True)
    game = models.ForeignKey(
        Game, null=True, blank=False, on_delete=models.CASCADE)
    card_family = models.ForeignKey(
        CardFamily, null=True, blank=False, on_delete=models.CASCADE)

    is_active = models.BooleanField(default=True)

    slug = models.CharField(max_length=30, db_index=True)
    card_description = models.CharField(max_length=250, default='')
    # card_type = models.CharField(
    #     max_length=25, choices=ChoicesTipoCarta, default="hero")
    # session = models.CharField(max_length=25, choices=ChoicesSession)

    top_left_value = models.IntegerField(default=0, null=True)
    top_right_value = models.IntegerField(default=0, null=True)
    bottom_left_value = models.IntegerField(default=0, null=True)
    bottom_right_value = models.IntegerField(default=0, null=True)

    card_image = models.ImageField(upload_to="cards", null=True, blank=True)
    card_image_mini = models.ImageField(
        upload_to="cards", null=True, blank=True)

    def __str__(self) -> str:
        return self.slug
