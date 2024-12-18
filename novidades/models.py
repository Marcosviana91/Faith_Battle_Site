from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.


class Artigo(models.Model):
    id = models.AutoField(primary_key=True)
    destaque = models.BooleanField(default=False)
    titulo = models.CharField(max_length=255)
    img_capa = models.ImageField(upload_to=f'artigos/', null=True, blank=True)
    data_hora_publicacao = models.DateTimeField(default=timezone.now, null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    conteudo = models.TextField()
    tag_version = models.CharField(max_length=20)

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        self.titulo = self.titulo.replace("/", "-")
        self.tag_version = self.tag_version.replace("/", "-")
        folder = f'{self.data_hora_publicacao.year}/{
            self.data_hora_publicacao.month}/{self.data_hora_publicacao.day}/'
        img_capa_extension = self.img_capa.name.split(".")[-1]
        if not self.img_capa:
            self.img_capa.name = f'{folder}/img_capa_{self.tag_version}_{self.data_hora_publicacao.timestamp()}_{img_capa_extension}'
        super().save(*args, **kwargs)


class Enquetes(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    data_hora_publicacao = models.DateTimeField(default=timezone.now, null=True, blank=True)
    max_dias = models.IntegerField(null=True, blank=True, default=7)
    min_votos_por_opcao = models.IntegerField(
        null=True, blank=True, default=50)
    encerrada = models.BooleanField(default=False)
    apoia = models.IntegerField(blank=True, default=0)
    nao_apoia = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.titulo
