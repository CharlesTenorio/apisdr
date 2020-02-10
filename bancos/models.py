from django.db import models


TIPO_CONTA = (
    ("Corrente", "Corrente"),
    ("Poupança", "Poupança"),

)


class Banco(models.Model):
    banco = models.CharField(max_length=50, unique=True)
    numero_banco = models.CharField(max_length=10, unique=True)
    ativo = models.BooleanField("Ativo", default=False)

    class Meta:
        ordering = ('banco',)

    def __str__(self):
        return self.banco
