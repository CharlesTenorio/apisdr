from django.contrib import admin
from .models import Epecialidade


class EspecialidadeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome',)
    search_fields = ('nome',)


admin.site.register(Epecialidade, EspecialidadeAdmin)
