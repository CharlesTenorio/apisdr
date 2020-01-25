from django.contrib import admin
from .models import Clinica


class ClinicaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'fone', 'fone1')
    search_fields = ('nome', 'email')


admin.site.register(Clinica, ClinicaAdmin)
