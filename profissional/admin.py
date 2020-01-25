from django.contrib import admin
from .models import Profissional


class ProfiAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'fone', 'nascimento')


admin.site.register(Profissional, ProfiAdmin)
