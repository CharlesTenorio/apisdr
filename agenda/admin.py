from django.contrib import admin
from .models import Agendamento


class AgendaAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_clinica_profi', 'id_horario', 'id_cliente')
    list_filter = ('status_agenda',)


admin.site.register(Agendamento, AgendaAdmin)
