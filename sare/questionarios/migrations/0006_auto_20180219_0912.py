# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-19 12:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionarios', '0005_auto_20180218_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionario',
            name='bairro',
            field=models.CharField(max_length=100, verbose_name='bairro'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='cor_raca',
            field=models.CharField(choices=[('1', 'Branca'), ('2', 'Amarela'), ('3', 'Parda'), ('4', 'Estrangeiro'), ('5', 'Preta'), ('6', 'Afro descendente Quilombola'), ('7', 'Indígena'), ('8', 'Estrangeiro refugiado')], max_length=1, verbose_name='Como você considera sua cor/raça?'),
        ),
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
            name='despesas_transporte',
            field=models.FloatField(verbose_name='Transporte'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='fale_mais_familia',
            field=models.CharField(max_length=500, verbose_name='Fale mais sobre sua família'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='pne_def_fisica',
            field=models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], max_length=1, verbose_name='Possui deficiência física?'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='pne_def_mental_grave',
            field=models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], max_length=1, verbose_name='Tem deficiência mental grave?'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='pne_def_mental_leve',
            field=models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], max_length=1, verbose_name='Tem deficiência mental leve?'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='pne_parcial_visao_audicao',
            field=models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], max_length=1, verbose_name='Tem deficiência parcial de visão/audição?'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='pne_total_visao_audicao',
            field=models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], max_length=1, verbose_name='Tem deficiência total  de visão/audição?'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='preconceito_cultural',
            field=models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], max_length=1, verbose_name='Cultural'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='preconceito_economico',
            field=models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], max_length=1, verbose_name='Econômico'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='preconceito_estetico',
            field=models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], max_length=1, verbose_name='Estético'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='preconceito_genero',
            field=models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], max_length=1, verbose_name='Gênero'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='preconceito_mental',
            field=models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], max_length=1, verbose_name='Mental'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='preconceito_orientacao_sexual',
            field=models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], max_length=1, verbose_name='Orientação sexual'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='preconceito_racial',
            field=models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], max_length=1, verbose_name='Racial'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='preconceito_religioso',
            field=models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], max_length=1, verbose_name='Religioso'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='psico_conflito_familiar',
            field=models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], max_length=1, verbose_name='Vivencia algum problema/conflito familiar'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='psico_depressao',
            field=models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], max_length=1, verbose_name='Sofre de depressão?'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='psico_dificuldade_concentrar',
            field=models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], max_length=1, verbose_name='Sente dificuldade em se concentrar?'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='renda_per_capita',
            field=models.CharField(choices=[(1, '1.405,51 (a partir)'), (2, '937,01 a 1405,50'), (3, '468,50 a 937,00'), (4, '234,25 até 468,49'), (5, 'de 0 até 234, 24')], max_length=1, verbose_name='Faixa de renda'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='saude_bebida_drogas',
            field=models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], max_length=1, verbose_name='Faz uso, abuso de bebida alcóolica e/ou drogas?'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='saude_doenca_cronica',
            field=models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], max_length=1, verbose_name='Possui doença crônica?'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='saude_doenca_grave',
            field=models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], max_length=1, verbose_name='Possui doença grave'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='saude_medicamento_diario',
            field=models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], max_length=1, verbose_name='Faz uso de medicamento diário, de impacto na renda familiar'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='violencia_abandono',
            field=models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], max_length=1, verbose_name='Negligência / abandono familiar'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='violencia_abuso_familiar',
            field=models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], max_length=1, verbose_name='Abuso por parte de familiares ou pessoas conhecidas'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='violencia_assedio_moral',
            field=models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], max_length=1, verbose_name='Assédio Moral'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='violencia_atentado_pudor',
            field=models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], max_length=1, verbose_name='Atentado ao pudor'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='violencia_cyberbulling',
            field=models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], max_length=1, verbose_name='Cyberbulling (por meio de redes sociais)'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='violencia_fisica',
            field=models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], max_length=1, verbose_name='Física'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='violencia_patrimonial',
            field=models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], max_length=1, verbose_name='Patrimonial/financeira'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='violencia_psicologica_moral',
            field=models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], max_length=1, verbose_name='Psicológica / moral'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='violencia_religiosa',
            field=models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], max_length=1, verbose_name='Religiosa'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='violencia_sexual',
            field=models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], max_length=1, verbose_name='Sexual'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='violencia_trafico_humano',
            field=models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], max_length=1, verbose_name='Tráfico de seres humanos'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='violencia_urbana',
            field=models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], max_length=1, verbose_name='Violência urbana(assalto, transito, etc)'),
        ),
        migrations.AlterField(
            model_name='questionario',
            name='violencia_verbal',
            field=models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], max_length=1, verbose_name='Verbal(xingamentos, desacatos, etc.)'),
        ),
    ]
