from django.contrib import admin
from .models import Cliente


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'nascimento', 'fone')
    search_fields = ('nome', 'email')


admin.site.register(Cliente, ClienteAdmin)
