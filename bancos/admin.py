from django.contrib import admin
from .models import Banco


class BancoAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero_banco', 'banco')
    search_fields = ('banco',)


admin.site.register(Banco, BancoAdmin)
