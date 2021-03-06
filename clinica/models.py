from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from cloudinary.models import CloudinaryField
from django.db.models.signals import pre_save
from django.dispatch import receiver
from bancos.models import Banco

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


class Subordinado(models.Model):
    id_usuario = models.OneToOneField(User, on_delete=models.PROTECT)
    id_banco = models.ForeignKey(Banco, on_delete=models.PROTECT, null=True, blank=True)
    razao_social = models.CharField(max_length=100)
    nome_fantasia = models.CharField(max_length=100)
    numero_documento = models.CharField(max_length=32)
    tipo_documento = models.CharField(max_length=20, default='CPF')
    mcc = models.CharField(max_length=6, default='8999', null=True)
    nome_contato = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=150)
    codigo_banco = models.CharField(max_length=20, default='')
    tipo_conta = models.CharField(max_length=40, choices=settings.CONTA_TIPO_CHOICES, default='CheckingAccount')
    numero_conta = models.CharField(max_length=30, default='')
    dig_verif = models.CharField(max_length=5, default='')
    agencia = models.CharField(max_length=10, default='')
    digito_agencia = models.CharField(max_length=5, default='')
    documento_conta = models.CharField(max_length=200, default='')
    tipo_doc_conta = models.CharField(max_length=30, default='')
    librar_para_braspg = models.BooleanField(default=False)

    def __str__(self):
        return self.nome_fantasia


def cadastro_subordinado(id_motorista, razao_social, nome_fantasia, numero_documento,
                         nome_contato, telefone, email):
    try:

        user = User.objects.filter(email=email).first()
        sub = Subordinado.objects.filter(id_usuario=user.id).first()

        if not sub:
            if not numero_documento:
                numero_documento = '123456'
            subordinado = Subordinado.objects.create(id_usuario=user,
                                                     razao_social=razao_social,
                                                     nome_fantasia=nome_fantasia,
                                                     numero_documento=numero_documento,
                                                     tipo_documento='',
                                                     mcc='8999',
                                                     nome_contato=nome_contato,
                                                     telefone=telefone,
                                                     email=email, codigo_banco='',
                                                     tipo_conta='',
                                                     numero_conta='',
                                                     dig_verif='',
                                                     agencia='',
                                                     digito_agencia='',
                                                     documento_conta='',
                                                     tipo_doc_conta='')

    except Exception as e:
        print(subordinado)
        print(str(e))
