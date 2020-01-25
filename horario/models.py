from django.db import models
from clinica_profissional.models import ClinicaProfissional
from django.conf import settings


class HorarioAgenda(models.Model):
    id_clinica_profi = models.ForeignKey(ClinicaProfissional, on_delete=models.PROTECT)
    dia_semana = models.CharField(max_length=20, choices=settings.DIAS_CHOICES)
    hora_inicial = models.TimeField()
    hora_final = models.TimeField()
    duracao = models.PositiveIntegerField()
    ativado = models.BooleanField(default=True)
    obs = models.TextField(max_length=300, null=True, blank=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
