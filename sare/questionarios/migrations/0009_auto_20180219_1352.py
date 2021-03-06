# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-19 16:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionarios', '0008_auto_20180219_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionario',
            name='despesas_bens_fcarro',
            field=models.FloatField(verbose_name='Parcela Carro'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='despesas_bens_fmoto',
            field=models.FloatField(verbose_name='Parcela Moto'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='despesas_bens_terreno',
            field=models.FloatField(verbose_name='Parcela Terreno'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='despesas_domesticas_agua',
            field=models.FloatField(verbose_name='Água e esgoto'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='despesas_domesticas_alimentacao',
            field=models.FloatField(verbose_name='Alimentação'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='despesas_domesticas_eletrica',
            field=models.FloatField(verbose_name='Energia elétrica'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='despesas_educacao_basico',
            field=models.FloatField(verbose_name='Ensino Fundamental'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='despesas_educacao_capacitacao',
            field=models.FloatField(verbose_name='Cursos de Capacitação'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='despesas_educacao_cursinho',
            field=models.FloatField(verbose_name='Cursinhos'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='despesas_educacao_material',
            field=models.FloatField(verbose_name='Material escolar'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='despesas_educacao_superior',
            field=models.FloatField(verbose_name='Graduação'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='despesas_moradia',
            field=models.FloatField(verbose_name='Moradia'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='despesas_saude_cuidador',
            field=models.FloatField(verbose_name='Cuidador de idoso/criança'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='despesas_saude_medicamento',
            field=models.FloatField(verbose_name='Medicamentos'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='despesas_saude_plano',
            field=models.FloatField(verbose_name='Plano de saúde'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='despesas_saude_tratamento',
            field=models.FloatField(verbose_name='Tratamento de Saúde'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='despesas_transporte',
            field=models.FloatField(verbose_name='Transporte'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='relacao_financeira',
            field=models.CharField(choices=[(1, 'É independente financeiramente'), (2, 'É independente financeiramente e responsável por parte das despesas domésticas'), (3, 'É independente totalmente e responsável por todas as despesas domésticas'), (4, 'Dependente inteiramente da renda dos pais ou companheiro(s)'), (5, 'Dependente inteiramente da renda de outros parentes')], default=None, max_length=1),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='renda_bruta_domiciliar',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='renda_per_capita',
            field=models.CharField(choices=[(1, '1.405,51 (a partir)'), (2, '937,01 a 1405,50'), (3, '468,50 a 937,00'), (4, '234,25 até 468,49'), (5, 'de 0 até 234, 24')], default=None, max_length=1, verbose_name='Faixa de renda'),
        ),
    ]
