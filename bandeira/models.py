from django.db import models
from cloudinary.models import CloudinaryField


class Bandeira(models.Model):
    bandeira = models.CharField(max_length=40, unique=True)
    img_bandeira = CloudinaryField('Imagem do cartao')

    def __str__(self):
        return self.bandeira
