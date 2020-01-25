from django.db import models
from cloudinary.models import CloudinaryField


class Epecialidade(models.Model):
    nome = models.CharField(max_length=80, unique=True)
    imagem = CloudinaryField('icone', null=True, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome
