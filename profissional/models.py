from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from cloudinary.models import CloudinaryField
from django.db.models.signals import pre_save
from django.dispatch import receiver
from random import randint

User = get_user_model()


class Profissional(models.Model):
    id_usuario = models.OneToOneField(
        User, on_delete=models.PROTECT, blank=True, null=True)
    nome = models.CharField(max_length=80)
    nascimento = models.DateField()
    sexo = models.CharField(max_length=10, choices=settings.SEXO_CHOICES)
    imagem = CloudinaryField('Foto de Perfil', null=True, blank=True)
    login_social = models.CharField(max_length=80, blank=True, null=True)
    fone = models.CharField(max_length=15, unique=True)
    pontuacao = models.FloatField(default=0)
    token = models.CharField(max_length=250, blank=True, null=True, default='ST')
    cpf = models.CharField(max_length=14)
    cosenho = models.CharField(max_length=30)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)
    imagem = CloudinaryField('Foto de Perfil', null=True, blank=True)
    email = models.EmailField(max_length=150, unique=True)
    senha = models.CharField(max_length=150)
    confirma_sms = models.BooleanField(default=False)
    token_fcm = models.CharField(max_length=250, null=True, blank=True)
    mini_curriculum = models.TextField(max_length=1000, blank=True, null=True)

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome


# TODO decodificar o token para pegar id
@receiver(pre_save, sender=Profissional)
def pegar_usuario_id(sender, instance, **kwargs):
    if instance.num_verificacao == '':
        instance.num_verificacao = str(gera_codigo_confirmacao(4))
    usr = User.objects.filter(username=instance.email).first()
    instance.id_usuario = usr


def gera_codigo_confirmacao(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)
