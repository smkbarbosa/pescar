from django.contrib import admin
from django.utils.timezone import now

from sare.questionarios.models import Questionario, DimensaoEconomica, \
    DimensaoSocial, DimensaoCultural, \
    DimensaoAmbiental, QuestionarioOld


class EconomicaAdmin(admin.StackedInline):
    model = DimensaoEconomica
    list_display = ['_all_']
    extra = 0


class SocialAdmin(admin.StackedInline):
    model = DimensaoSocial
    extra = 0


class CulturalAdmin(admin.StackedInline):
    model = DimensaoCultural
    extra = 0


class AmbientalAdmin(admin.StackedInline):
    model = DimensaoAmbiental
    extra = 0


#@admin.register(Questionario)
class QuestionarioModelAdmin(admin.ModelAdmin):
    exclude = ['nome', 'economica', 'cultural', 'social', 'ambiental']
    list_display = ('nome', 'email', 'cpf', 'curso', 'criado_em', 'preenchido_hoje')
    readonly_fields = ['nome', 'aluno','fale_mais_familia']
    inlines = [EconomicaAdmin, SocialAdmin, CulturalAdmin, AmbientalAdmin]
    date_hierarchy = 'criado_em'
    search_fields = ('aluno__nome', 'aluno__email', 'aluno__cpf', 'aluno__curso', 'criado_em')
    list_filter = ('criado_em', )


    def nome(self, obj):
        return obj.aluno.nome

    def email(self, obj):
        return obj.aluno.email

    def cpf(self, obj):
        return obj.aluno.cpf

    def curso(self, obj):
        return obj.aluno.get_curso_display()

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


@admin.register(QuestionarioOld)
class QuestionarioOldAdmin(admin.ModelAdmin):
    list_display = (
    'nome', 'email', 'cpf', 'curso', 'criado_em', 'preenchido_hoje')
    date_hierarchy = 'criado_em'
    search_fields = (
    'nome', 'email', 'cpf', 'curso', 'criado_em')
    list_filter = ('criado_em',)

    def nome(self, obj):
        return obj.nome

    def email(self, obj):
        return obj.email

    def cpf(self, obj):
        return obj.cpf

    def curso(self, obj):
        return obj.get_curso_display()

    def preenchido_hoje(self, obj):
        return obj.criado_em.date() == now().date()

    preenchido_hoje.short_description = 'respondeu hoje?'
    preenchido_hoje.boolean = True

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return [f.name for f in self.model._meta.fields]
        return super(QuestionarioOldAdmin, self).get_readonly_fields(
            request, obj=obj
            )

# admin.site.register(Questionario, QuestionarioModelAdmin)


