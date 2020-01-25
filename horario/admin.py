from django.contrib import admin
from .models import HorarioAgenda


class HorarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'dia_semana', 'hora_inicial', 'hora_final')


admin.site.register(HorarioAgenda, HorarioAdmin)
