from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from cloudinary.models import CloudinaryField
from django.db.models.signals import pre_save
from django.dispatch import receiver

User = get_user_model()


class Clinica(models.Model):
    id_usuario = models.OneToOneField(User, on_delete=models.PROTECT, blank=True, null=True)
    nome = models.CharField(max_length=80)
    cep = models.CharField("CEP *", max_length=10)
    logradouro = models.CharField("Logradouro *", max_length=80)
    numero = models.CharField("Número *", max_length=5)
    complemento = models.CharField(max_length=30, null=True, blank=True)
    bairro = models.CharField("Bairro *", max_length=40)
    localidade = models.CharField("Cidade *", max_length=50)
    uf = models.CharField("Estado *", max_length=2, default='PE', choices=settings.ESTADOS_CHOICES)
    fone = models.CharField(max_length=15)
    fone1 = models.CharField(max_length=15, null=True, blank=True)
    fone2 = models.CharField(max_length=15, null=True, blank=True)
    pontuacao = models.FloatField(default=0)
    token = models.CharField(max_length=250, blank=True, null=True, default='ST')
    cnpj = models.CharField(max_length=14, unique=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)
    imagem = CloudinaryField('Foto de Perfil', null=True, blank=True)
    email = models.EmailField(max_length=150, unique=True)
    senha = models.CharField(max_length=150)
    token_fcm = models.CharField(max_length=250, null=True, blank=True)
    data_cad = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('nome', 'email',)

    def __str__(self):
        return self.nome


# TODO decodificar o token para pegar id
@receiver(pre_save, sender=Clinica)
def pegar_usuario_id(sender, instance, **kwargs):
    usr = User.objects.filter(username=instance.email).first()
    instance.id_usuario = usr
