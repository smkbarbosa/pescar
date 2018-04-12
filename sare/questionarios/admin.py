from django.contrib import admin
from django.utils.timezone import now

from sare.questionarios.models import QuestionarioOld


class QuestionarioModelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cpf', 'curso', 'criado_em', 'preenchido_hoje')
    date_hierarchy = 'criado_em'
    search_fields = ('nome', 'email', 'cpf', 'curso', 'criado_em')
    list_filter = ('criado_em', 'curso')

    def preenchido_hoje(self, obj):
        return obj.criado_em.date() == now().date()

    preenchido_hoje.short_description = 'respondeu hoje?'
    preenchido_hoje.boolean = True

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return [f.name for f in self.model._meta.fields]
        return super(QuestionarioModelAdmin, self).get_readonly_fields(
                request, obj=obj
        )


admin.site.register(QuestionarioOld, QuestionarioModelAdmin)

