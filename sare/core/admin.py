from django.contrib import admin

# Register your models here.
from sare.core.models import Aluno


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'cpf', 'fone', 'curso']
    search_fields = ('nome', 'cpf')