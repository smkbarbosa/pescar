from django.contrib import admin
from django.utils.timezone import now

from sare.questionarios.models import Questionario


class QuestionarioModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cpf', 'criado_em', 'preenchido_hoje')
    date_hierarchy = 'criado_em'
    search_fields = ('nome', 'email', 'cpf', 'criado_em')
    list_filter = ('criado_em',)

    def preenchido_hoje(self, obj):
        return obj.criado_em == now().date()

    preenchido_hoje.short_description = 'respondeu hoje?'
    preenchido_hoje.boolean = True

admin.site.register(Questionario, QuestionarioModelAdmin)
