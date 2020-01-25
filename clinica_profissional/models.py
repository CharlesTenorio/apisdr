from django.db import models
from profissional.models import Profissional
from clinica.models import Clinica


class ClinicaProfissional(models.Model):
    id_clinica = models.ForeignKey(Clinica, on_delete=models.PROTECT)
    id_profi = models.ForeignKey(Profissional, on_delete=models.PROTECT)
    profi_ativo = models.BooleanField(default=True)
