# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from sare.entrevista.models import Entrevista
from sare.entrevista.forms import EntrevistaForm
# Register your models here.


@admin.register(Entrevista)
class EntrevistaAdmin(admin.ModelAdmin):
    form = EntrevistaForm
    model = Entrevista

    fieldsets = [
        ('Informações do entrevistado', {'fields':[
            'aluno',
        ]}),
        ('Classificação de renda percapita', {'fields':[
            'per_renda_bruta',
            'per_dependentes',
            'per_imposto_renda',
            'per_previdencia'
        ]}),
        ('Despesas', {'fields':[
            (
                'd_tratamento_saude',
                'd_medicamentos',
                'd_cuidador',
                'd_plano_saude',
                'd_educacao_superior',
                'd_ensino_basico',
                'd_cursos_prep',
                'd_capacitacao',
            ),
            (
                'd_transporte',
                'd_aluguel',
                'd_financiamento_carro',
                'd_financiamento_moto',
                'd_terreno',
                'd_energia',
                'd_agua',
                'd_alimentacao'
            )
        ]}),
        ('Checklist de Documentos', {'fields':[
            'cl_1',
            'cl_2',
            'cl_3',
            'cl_4',
            'cl_5',
            'cl_6',
            'cl_7',
            'cl_8',
            'cl_9',
            'cl_10',
            'cl_11'
        ]}),
        ('Situações Problemas', {'fields':[
            'sp_1',
            'sp_2',
            'sp_3',
            'sp_4',
            'sp_5',
            'sp_6',
            'sp_7',
            'sp_8',
            'sp_9',
            'sp_10',
            'sp_11',
            'sp_12',
            'sp_13',
            'sp_14',
            'sp_15',
            'sp_16'
        ]}),
        ('Finalização da Entrevista', {'fields':[
            'fn_1',
            'fn_2',
            'fn_3',
            'fn_4',
            'fn_5',
            'fn_6',
            'fn_7',
        ]})
    ]


