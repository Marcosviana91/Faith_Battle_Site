# Generated by Django 5.1 on 2024-11-04 15:35

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(default='')),
                ('image', models.ImageField(blank=True, null=True, upload_to='games')),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CardFamily',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('short_description', models.CharField(max_length=255)),
                ('card_back_image', models.ImageField(blank=True, null=True, upload_to='cards')),
                ('top_left_txt', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('top_right_txt', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('bottom_left_txt', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('bottom_right_txt', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('deck_position_X', models.IntegerField(blank=True, null=True)),
                ('deck_position_Y', models.IntegerField(blank=True, null=True)),
                ('game', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='games.game')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('slug', models.CharField(db_index=True, max_length=30)),
                ('card_description', models.CharField(default='', max_length=250)),
                ('top_left_value', models.IntegerField(default=0)),
                ('top_right_value', models.IntegerField(default=0)),
                ('bottom_left_value', models.IntegerField(default=0)),
                ('bottom_right_value', models.IntegerField(default=0)),
                ('card_image', models.ImageField(blank=True, null=True, upload_to='cards')),
                ('card_image_mini', models.ImageField(blank=True, null=True, upload_to='cards')),
                ('card_family', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='games.cardfamily')),
                ('game', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='games.game')),
            ],
        ),
        migrations.CreateModel(
            name='GameBoard',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=30)),
                ('image', models.ImageField(blank=True, null=True, upload_to='game_boards')),
                ('game', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='games.game')),
            ],
        ),
    ]
