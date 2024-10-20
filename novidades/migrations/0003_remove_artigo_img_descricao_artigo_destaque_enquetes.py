# Generated by Django 5.1 on 2024-10-14 02:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novidades', '0002_remove_artigo_data_publicacao_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artigo',
            name='img_descricao',
        ),
        migrations.AddField(
            model_name='artigo',
            name='destaque',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Enquetes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=255)),
                ('descricao', models.TextField()),
                ('data_hora_publicacao', models.DateTimeField(blank=True, null=True)),
                ('max_dias', models.IntegerField(blank=True, default=7, null=True)),
                ('min_votos_por_opcao', models.IntegerField(blank=True, default=50, null=True)),
                ('encerrada', models.BooleanField(default=False)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
