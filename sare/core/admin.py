from django.contrib import admin

# Register your models here.
from sare.core.models import Aluno


class AlunoModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'campus', 'curso', 'matricula')
    search_fields = ('nome', 'curso')
    list_filter = ('curso', 'campus')


admin.site.register(Aluno, AlunoModelAdmin)