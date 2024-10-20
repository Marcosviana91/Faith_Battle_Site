# Generated by Django 5.1 on 2024-10-19 14:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_cardfamily'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('slug', models.CharField(db_index=True, max_length=30, unique=True)),
                ('card_description', models.CharField(default='', max_length=250)),
                ('wisdom_cost', models.IntegerField(default=0)),
                ('attack_point', models.IntegerField(default=0)),
                ('defense_points', models.IntegerField(default=0)),
                ('card_image', models.ImageField(blank=True, null=True, upload_to='cards')),
                ('card_image_mini', models.ImageField(blank=True, null=True, upload_to='cards')),
                ('card_family', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='games.cardfamily')),
            ],
        ),
    ]