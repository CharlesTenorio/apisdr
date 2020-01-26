from django.db import models
from profissional.models import Profissional


class Marcacao(models.Model):
    id_profissional = models.ForeignKey(Profissional, on_delete=models.PROTECT)
    data_cadastro = models.DateTimeField(auto_created=True)
