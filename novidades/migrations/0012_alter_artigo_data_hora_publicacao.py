# Generated by Django 5.1 on 2024-10-23 16:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novidades', '0011_alter_artigo_data_hora_publicacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artigo',
            name='data_hora_publicacao',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 10, 23, 16, 48, 48, 194293, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
