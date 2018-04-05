# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-05 18:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('questionarios', '0031_auto_20180301_1348'),
    ]

    operations = [
        migrations.CreateModel(
            name='DimensaoAmbiental',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicos_indisponiveis_bairro', models.CharField(choices=[('1', 'Táxi'), ('2', 'Moto táxi'), ('3', 'Transporte escolar pago'), ('4', 'Ônibus escolar'), ('5', 'Transporte escolar público'), ('6', 'Ônibus coletivo')], default=None, max_length=20, null=True)),
                ('forma_descarte_lixo', models.CharField(choices=[('1', 'Serviço público de limpeza'), ('3', 'Jogado em terreno baldio ou em via pública'), ('2', 'Enterrado'), ('4', 'Queimado')], default=None, max_length=1)),
                ('percepcao_seguranca_bairro', models.CharField(choices=[('1', 'Não oferece risco de segurança aos seus moradores'), ('4', 'É considerado perigoso e os moradores sofrem  com a criminalidade'), ('2', 'Os moradores se sentem seguros (há policiamento nas ruas)'), ('5', 'Frequentemente os moradores sofrem  algum tipo de violência no bairro ou nos arredores'), ('3', 'Não há registro de violência sofrida pelo moradores do bairro')], default=None, max_length=1)),
                ('problemas_bairro', models.CharField(choices=[('1', 'Abastecimento de água'), ('2', 'Alagamentos'), ('3', 'Pavimentação (asfalto nas ruas)'), ('4', 'Energia e iluminação pública'), ('5', 'Ruas esburacadas (erosão)'), ('6', 'Saneamento básico (esgoto)'), ('7', 'Serviços de segurança'), ('8', 'Acessibilidade '), ('9', 'Áreas de recreaçao e lazer'), ('10', 'Limpeza e coleta de lixo'), ('11', 'Serviços de saúde'), ('12', 'Transporte público')], default=None, max_length=20, null=True)),
                ('fale_mais_familia', models.CharField(max_length=500, verbose_name='Fale mais sobre sua família')),
            ],
            options={
                'verbose_name': 'dimensão ambiental',
            },
        ),
        migrations.CreateModel(
            name='DimensaoCultural',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cor_raca', models.CharField(choices=[('1', 'Branca'), ('2', 'Amarela'), ('3', 'Parda'), ('4', 'Estrangeiro'), ('5', 'Preta'), ('6', 'Afro descendente Quilombola'), ('7', 'Indígena'), ('8', 'Estrangeiro refugiado')], default=None, max_length=1, verbose_name='Como você considera sua cor/raça?')),
                ('violencia_verbal', models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], default=None, max_length=1, verbose_name='Verbal(xingamentos, desacatos, etc.)')),
                ('violencia_urbana', models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], default=None, max_length=1, verbose_name='Violência urbana(assalto, transito, etc)')),
                ('violencia_patrimonial', models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], default=None, max_length=1, verbose_name='Patrimonial/financeira')),
                ('violencia_cyberbulling', models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], default=None, max_length=1, verbose_name='Cyberbulling (por meio de redes sociais)')),
                ('violencia_religiosa', models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], default=None, max_length=1, verbose_name='Religiosa')),
                ('violencia_assedio_moral', models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], default=None, max_length=1, verbose_name='Assédio Moral')),
                ('violencia_abandono', models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], default=None, max_length=1, verbose_name='Negligência / abandono familiar')),
                ('violencia_abuso_familiar', models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], default=None, max_length=1, verbose_name='Abuso por parte de familiares ou pessoas conhecidas')),
                ('violencia_atentado_pudor', models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], default=None, max_length=1, verbose_name='Atentado ao pudor')),
                ('violencia_trafico_humano', models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], default=None, max_length=1, verbose_name='Tráfico de seres humanos')),
                ('violencia_psicologica_moral', models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], default=None, max_length=1, verbose_name='Psicológica / moral')),
                ('violencia_fisica', models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], default=None, max_length=1, verbose_name='Física')),
                ('violencia_sexual', models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], default=None, max_length=1, verbose_name='Sexual')),
                ('preconceito_cultural', models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], default=None, max_length=1, verbose_name='Cultural')),
                ('preconceito_estetico', models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], default=None, max_length=1, verbose_name='Estético')),
                ('preconceito_economico', models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], default=None, max_length=1, verbose_name='Econômico')),
                ('preconceito_religioso', models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], default=None, max_length=1, verbose_name='Religioso')),
                ('preconceito_mental', models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], default=None, max_length=1, verbose_name='Mental')),
                ('preconceito_racial', models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], default=None, max_length=1, verbose_name='Racial')),
                ('preconceito_genero', models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], default=None, max_length=1, verbose_name='Gênero')),
                ('preconceito_orientacao_sexual', models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], default=None, max_length=1, verbose_name='Orientação sexual')),
            ],
            options={
                'verbose_name': 'dimensão cultural',
            },
        ),
        migrations.CreateModel(
            name='DimensaoEconomica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dependentes_RBD', models.IntegerField(verbose_name='Dependentes da Renda Bruta Domiciliar')),
                ('origem_renda', models.IntegerField(verbose_name='Quantidade de pessoas que possuem renda')),
                ('renda_bruta_domiciliar', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('responsavel_domicilio', models.CharField(max_length=100)),
                ('renda_per_capita', models.CharField(choices=[('1', '1.431,01 (a partir)'), ('2', '954,01 a 1431,00'), ('3', '477,01 a 954,00'), ('4', '238,50 até 477,00'), ('5', 'de 0 até 238, 49')], default=None, max_length=1, verbose_name='Faixa de renda')),
                ('relacao_financeira', models.CharField(choices=[('1', 'É independente financeiramente'), ('2', 'É independente financeiramente e responsável por parte das despesas domésticas'), ('3', 'É independente totalmente e responsável por todas as despesas domésticas'), ('4', 'Dependente inteiramente da renda dos pais ou companheiro(s)'), ('5', 'Dependente inteiramente da renda de outros parentes')], default=None, max_length=1)),
                ('despesas_saude_tratamento', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Tratamento de Saúde')),
                ('despesas_saude_medicamento', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Medicamentos')),
                ('despesas_saude_cuidador', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Cuidador de idoso/criança')),
                ('despesas_saude_plano', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Plano de saúde')),
                ('despesas_transporte', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Transporte')),
                ('despesas_moradia', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Moradia')),
                ('despesas_educacao_superior', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Graduação')),
                ('despesas_educacao_basico', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Ensino Fundamental')),
                ('despesas_educacao_cursinho', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Cursinhos')),
                ('despesas_educacao_capacitacao', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Cursos de Capacitação')),
                ('despesas_educacao_material', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Material escolar')),
                ('despesas_bens_fcarro', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Parcela Carro')),
                ('despesas_bens_fmoto', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Parcela Moto')),
                ('despesas_bens_terreno', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Parcela Terreno')),
                ('despesas_domesticas_eletrica', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Energia elétrica')),
                ('despesas_domesticas_agua', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Água e esgoto')),
                ('despesas_domesticas_alimentacao', models.DecimalField(decimal_places=2, default=0.0, max_digits=8, verbose_name='Alimentação')),
            ],
            options={
                'verbose_name': 'dimensão econômica',
            },
        ),
        migrations.CreateModel(
            name='DimensaoSocial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condicao_responsavel_casa', models.CharField(choices=[('1', 'Servidor Público'), ('2', 'Trabalhador contribuinte'), ('3', 'Trabalhador empregado (CLT)'), ('4', 'Trabalhador informal (s/ contrib)'), ('5', 'Desempregado')], default=None, max_length=1)),
                ('meio_acesso_campus', models.CharField(choices=[('1', 'Próprio (carro)'), ('2', 'Próprio (moto)'), ('3', 'Carona (sem contribuição)'), ('4', 'Coletivo público (não paga passagem)'), ('5', 'Vai a pé'), ('6', 'Vai de bicicleta'), ('7', 'Carona (com contribuição)'), ('8', 'Coletivo público (paga passagem)'), ('9', 'Alternativo (van, etc)')], default=None, max_length=1)),
                ('condicao_moradia', models.CharField(choices=[('1', 'Herança'), ('2', 'Própria da família (quitada)'), ('3', 'Própria da família (adquirida por meio de projeto social de habitação, com pagamento de parcelas)'), ('4', 'Própria da família (financiada)'), ('5', 'Cedida (gratuita)'), ('6', 'Própria da família (adquirida por meio de projeto social de habitação, quitada)'), ('7', 'Alugada'), ('8', 'Com terceiros (sem contribuição)'), ('9', 'Com terceiros (com contribuição)'), ('10', 'Ocupação')], default=None, max_length=2)),
                ('local_moradia', models.CharField(choices=[('1', 'Zona Urbana'), ('2', 'Zona Rural (fazenda, chácara, sítio)'), ('3', 'Zona Rural (indígena, quilombola, assentamento)'), ('4', 'Área de risco (inundação, deslizamento, ocupação, etc)')], default=None, max_length=1)),
                ('total_pessoas_casa', models.CharField(choices=[('1', 'De 1 a 2 pessoas'), ('2', 'De 3 a 5 pessoas'), ('3', 'De 6 a 8 pessoas'), ('4', 'Acima de 9 pessoas')], default=None, max_length=1)),
                ('total_comodos_casa', models.CharField(choices=[('1', 'Acima de 9 cômodos'), ('2', 'De 6 a 8 cômodos'), ('3', 'De 3 a 5 cômodos'), ('4', 'De 1 a 2 cômodos')], default=None, max_length=1)),
                ('total_km_casa_campus', models.CharField(choices=[('1', '5 km (até)'), ('2', '6 a 10 km'), ('3', '11 a 25 km'), ('4', '26 km (acima de)')], default=None, max_length=1)),
                ('instituicao_anterior', models.CharField(choices=[('1', 'Particular'), ('2', 'Bolsa total (mérito)'), ('3', 'Bolsa parcial (mérito)'), ('4', 'Bolsa parcial (vulnerabilidade)'), ('5', 'Bolsa total (vulnerabilidade)'), ('6', 'Pública')], default=None, max_length=1)),
                ('saude_bebida_drogas', models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], default=None, max_length=1, verbose_name='Faz uso, abuso de bebida alcóolica e/ou drogas?')),
                ('saude_doenca_grave', models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], default=None, max_length=1, verbose_name='Possui doença grave')),
                ('saude_doenca_cronica', models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], default=None, max_length=1, verbose_name='Possui doença crônica?')),
                ('saude_medicamento_diario', models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], default=None, max_length=1, verbose_name='Faz uso de medicamento diário, de impacto na renda familiar')),
                ('pne_parcial_visao_audicao', models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], default=None, max_length=1, verbose_name='Tem deficiência parcial de visão/audição?')),
                ('pne_def_fisica', models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], default=None, max_length=1, verbose_name='Possui deficiência física?')),
                ('pne_total_visao_audicao', models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], default=None, max_length=1, verbose_name='Tem deficiência total  de visão/audição?')),
                ('pne_def_mental_leve', models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], default=None, max_length=1, verbose_name='Tem deficiência mental leve?')),
                ('pne_def_mental_grave', models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], default=None, max_length=1, verbose_name='Tem deficiência mental grave?')),
                ('psico_dificuldade_concentrar', models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], default=None, max_length=1, verbose_name='Sente dificuldade em se concentrar?')),
                ('psico_conflito_familiar', models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], default=None, max_length=1, verbose_name='Vivencia algum problema/conflito familiar')),
                ('psico_depressao', models.CharField(choices=[('1', 'Você'), ('2', 'Família'), ('3', 'Ambos'), ('0', 'Não se aplica')], default=None, max_length=1, verbose_name='Sofre de depressão?')),
            ],
            options={
                'verbose_name': 'dimensão social',
            },
        ),
        migrations.AddField(
            model_name='questionario',
            name='aluno',
            field=models.ManyToManyField(to='core.Aluno'),
        ),
        migrations.AlterUniqueTogether(
            name='questionario',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='bairro',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='campus',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='cep',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='cidade',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='condicao_moradia',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='condicao_responsavel_casa',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='cor_raca',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='cpf',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='curso',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='dependentes_RBD',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='despesas_bens_fcarro',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='despesas_bens_fmoto',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='despesas_bens_terreno',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='despesas_domesticas_agua',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='despesas_domesticas_alimentacao',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='despesas_domesticas_eletrica',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='despesas_educacao_basico',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='despesas_educacao_capacitacao',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='despesas_educacao_cursinho',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='despesas_educacao_material',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='despesas_educacao_superior',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='despesas_moradia',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='despesas_saude_cuidador',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='despesas_saude_medicamento',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='despesas_saude_plano',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='despesas_saude_tratamento',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='despesas_transporte',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='email',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='endereco',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='fale_mais_familia',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='fone',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='forma_descarte_lixo',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='instituicao_anterior',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='local_moradia',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='matricula',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='meio_acesso_campus',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='num_casa',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='origem_renda',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='percepcao_seguranca_bairro',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='pne_def_fisica',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='pne_def_mental_grave',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='pne_def_mental_leve',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='pne_parcial_visao_audicao',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='pne_total_visao_audicao',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='preconceito_cultural',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='preconceito_economico',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='preconceito_estetico',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='preconceito_genero',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='preconceito_mental',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='preconceito_orientacao_sexual',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='preconceito_racial',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='preconceito_religioso',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='psico_conflito_familiar',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='psico_depressao',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='psico_dificuldade_concentrar',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='relacao_financeira',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='renda_bruta_domiciliar',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='renda_per_capita',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='responsavel_domicilio',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='saude_bebida_drogas',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='saude_doenca_cronica',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='saude_doenca_grave',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='saude_medicamento_diario',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='sem_mod_ano',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='sexo',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='total_comodos_casa',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='total_km_casa_campus',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='total_pessoas_casa',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='violencia_abandono',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='violencia_abuso_familiar',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='violencia_assedio_moral',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='violencia_atentado_pudor',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='violencia_cyberbulling',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='violencia_fisica',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='violencia_patrimonial',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='violencia_psicologica_moral',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='violencia_religiosa',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='violencia_sexual',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='violencia_trafico_humano',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='violencia_urbana',
        ),
        migrations.RemoveField(
            model_name='questionario',
            name='violencia_verbal',
        ),
        migrations.AddField(
            model_name='questionario',
            name='dimensao_ambiental',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='questionarios.DimensaoAmbiental'),
        ),
        migrations.AddField(
            model_name='questionario',
            name='dimensao_cultural',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='questionarios.DimensaoCultural'),
        ),
        migrations.AddField(
            model_name='questionario',
            name='dimensao_economica',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='questionarios.DimensaoEconomica'),
        ),
        migrations.AddField(
            model_name='questionario',
            name='dimensao_social',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='questionarios.DimensaoSocial'),
        ),
    ]
