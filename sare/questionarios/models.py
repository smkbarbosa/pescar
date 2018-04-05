import uuid

from django.db import models


# class QuestionarioOld(models.Model):
#     hashId = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
#     nome = models.CharField('nome', max_length=100)
#     cpf = models.CharField('CPF', max_length=14, validators=[cpf_is_digits, cpf_is_valid])
#     email = models.EmailField('e-mail')
#     fone = models.CharField('telefone',max_length=20, blank=True)
#
#     endereco = models.CharField('endereço', max_length=100, default=None)
#     num_casa = models.CharField('número da casa', max_length=4, default=0)
#     cep = models.CharField('cep', max_length=9, default=None)
#     bairro = models.CharField('bairro', max_length=100)
#     cidade = models.CharField('cidade', max_length=100)
#     estado = models.CharField('estado', max_length=2, default='TO')
#     sexo = models.CharField('sexo', max_length=1, choices=SEXO_CHOICES, default=None)
#
#     curso = models.CharField('curso', choices=CURSO_CHOICE, max_length=50, default=None)
#     sem_mod_ano = models.CharField('Semestre/Módulo/Ano', max_length=10, default=None)
#     matricula = models.CharField('matrícula', max_length=15, default=None)
#     campus = models.CharField('campus', max_length=30, default='PALMAS')
#
#     criado_em = models.DateTimeField('criado em', auto_now_add=True)
#
#     # Dimensão economica
#     dependentes_RBD = models.IntegerField('Dependentes da Renda Bruta Domiciliar', )
#     origem_renda = models.IntegerField('Quantidade de pessoas que possuem renda',)
#     renda_bruta_domiciliar = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
#     responsavel_domicilio = models.CharField(max_length=100)
#
#     # Finanças
#     renda_per_capita = models.CharField('Faixa de renda', max_length=1, choices=RENDA_PER_CAPITA_CHOICE, default=None)
#
#     relacao_financeira = models.CharField(choices=DEPENDENCIA_FINANCEIRA_CHOICE,
#                                           max_length=1, default=None)
#
#     # Despesas
#
#     despesas_saude_tratamento = models.DecimalField('Tratamento de Saúde', max_digits=8, decimal_places=2, default=0.0)
#     despesas_saude_medicamento = models.DecimalField('Medicamentos', max_digits=8, decimal_places=2, default=0.0)
#     despesas_saude_cuidador = models.DecimalField('Cuidador de idoso/criança', max_digits=8, decimal_places=2, default=0.0)
#     despesas_saude_plano = models.DecimalField('Plano de saúde', max_digits=8, decimal_places=2, default=0.0)
#
#     despesas_transporte = models.DecimalField('Transporte', max_digits=8, decimal_places=2, default=0.0)
#
#     despesas_moradia = models.DecimalField('Moradia', max_digits=8, decimal_places=2, default=0.0)
#
#     despesas_educacao_superior = models.DecimalField('Graduação', max_digits=8, decimal_places=2, default=0.0)
#     despesas_educacao_basico = models.DecimalField('Ensino Fundamental', max_digits=8, decimal_places=2, default=0.0)
#     despesas_educacao_cursinho = models.DecimalField('Cursinhos', max_digits=8, decimal_places=2, default=0.0)
#     despesas_educacao_capacitacao = models.DecimalField('Cursos de Capacitação', max_digits=8, decimal_places=2,
#                                                         default=0.0)
#     despesas_educacao_material = models.DecimalField('Material escolar', max_digits=8, decimal_places=2, default=0.0)
#
#     despesas_bens_fcarro = models.DecimalField('Parcela Carro', max_digits=8, decimal_places=2, default=0.0)
#     despesas_bens_fmoto = models.DecimalField('Parcela Moto', max_digits=8, decimal_places=2, default=0.0)
#     despesas_bens_terreno = models.DecimalField('Parcela Terreno', max_digits=8, decimal_places=2, default=0.0)
#
#     despesas_domesticas_eletrica = models.DecimalField('Energia elétrica', max_digits=8, decimal_places=2, default=0.0)
#     despesas_domesticas_agua = models.DecimalField('Água e esgoto', max_digits=8, decimal_places=2, default=0.0)
#     despesas_domesticas_alimentacao = models.DecimalField('Alimentação', max_digits=8, decimal_places=2, default=0.0)
#
#     # Dimensao Social
#     condicao_responsavel_casa = models.CharField(choices=CONDICAO_RESPONSAVEL_CASA_CHOICES, max_length=1, default=None)
#
#     meio_acesso_campus = models.CharField(choices=MEIO_ACESSO_CAMPUS_CHOICES, max_length=1, default=None)
#
#     condicao_moradia = models.CharField(choices=CONDICAO_MORADIA_CHOICES, max_length=2, default=None)
#
#     local_moradia = models.CharField(choices=LOCAL_MORADIA_CHOICES, max_length=1, default=None)
#
#     total_pessoas_casa = models.CharField(choices=TOTAL_PESSOAS_CHOICES, max_length=1, default=None)
#
#     total_comodos_casa = models.CharField(choices=TOTAL_COMODOS_CHOICES, max_length=1, default=None)
#
#     total_km_casa_campus = models.CharField(choices=TOTAL_KM_CHOICES, max_length=1, default=None)
#
#     instituicao_anterior = models.CharField(choices=INSTITUICAO_ANTERIOR_CHOICES, max_length=1, default=None)
#
#     S = ['Faz uso, abuso de bebida alcóolica e/ou drogas?', 'Possui doença grave', 'Possui doença crônica?',
#              'Faz uso de medicamento diário, de impacto na renda familiar'
#              ]
#
#     saude_bebida_drogas = models.CharField(S[0], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
#
#     saude_doenca_grave = models.CharField(S[1], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
#
#     saude_doenca_cronica = models.CharField(S[2], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
#
#     saude_medicamento_diario = models.CharField(S[3], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
#
#     PNE = [
#         'Tem deficiência parcial de visão/audição?',
#         'Possui deficiência física?',
#         'Tem deficiência total  de visão/audição?',
#         'Tem deficiência mental leve?',
#         'Tem deficiência mental grave?',
#     ]
#
#     PSI = [
#         'Sente dificuldade em se concentrar?',
#         'Vivencia algum problema/conflito familiar',
#         'Sofre de depressão?',
#     ]
#
#     pne_parcial_visao_audicao = models.CharField(PNE[0],choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
#     pne_def_fisica = models.CharField(PNE[1], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
#     pne_total_visao_audicao = models.CharField(PNE[2], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
#     pne_def_mental_leve = models.CharField(PNE[3], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
#     pne_def_mental_grave = models.CharField(PNE[4], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
#
#     psico_dificuldade_concentrar = models.CharField(PSI[0], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
#     psico_conflito_familiar = models.CharField(PSI[1], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
#     psico_depressao = models.CharField(PSI[2], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
#
#     ## Cultural
#
#     cor_raca = models.CharField('Como você considera sua cor/raça?', choices=COR_RACA_CHOICES, max_length=1, default=None)
#
#     V = [
#         'Verbal(xingamentos, desacatos, etc.)',
#         'Violência urbana(assalto, transito, etc)',
#         'Patrimonial/financeira',
#         'Cyberbulling (por meio de redes sociais)',
#         'Religiosa',
#         'Assédio Moral',
#         'Negligência / abandono familiar',
#         'Abuso por parte de familiares ou pessoas conhecidas',
#         'Atentado ao pudor',
#         'Tráfico de seres humanos',
#         'Psicológica / moral',
#         'Física',
#         'Sexual'
#     ]
#
#     violencia_verbal = models.CharField(V[0], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
#     violencia_urbana = models.CharField(V[1], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
#     violencia_patrimonial = models.CharField(V[2], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
#     violencia_cyberbulling = models.CharField(V[3], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
#     violencia_religiosa = models.CharField(V[4], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
#     violencia_assedio_moral = models.CharField(V[5], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
#     violencia_abandono = models.CharField(V[6], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
#     violencia_abuso_familiar = models.CharField(V[7], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
#     violencia_atentado_pudor = models.CharField(V[8], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
#     violencia_trafico_humano = models.CharField(V[9], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
#     violencia_psicologica_moral = models.CharField(V[10], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
#     violencia_fisica = models.CharField(V[11], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
#     violencia_sexual = models.CharField(V[12], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
#
#     PREC = [
#         'Cultural',
#         'Estético',
#         'Econômico',
#         'Religioso',
#         'Mental',
#         'Racial',
#         'Gênero',
#         'Orientação sexual'
#     ]
#
#     preconceito_cultural = models.CharField(PREC[0], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
#     preconceito_estetico = models.CharField(PREC[1], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
#     preconceito_economico = models.CharField(PREC[2], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
#     preconceito_religioso = models.CharField(PREC[3], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
#     preconceito_mental = models.CharField(PREC[4], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
#     preconceito_racial = models.CharField(PREC[5], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
#     preconceito_genero = models.CharField(PREC[6], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
#     preconceito_orientacao_sexual = models.CharField(PREC[7], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
#
#     # servicos_indisponiveis_bairro = models.CharField(choices=SERVICOS_INDISPONIVEIS_CHOICES, max_length=20, default=None, null=True)
#
#     forma_descarte_lixo = models.CharField(choices=DESCARTE_LIXO_CHOICE, max_length=1, default=None)
#
#     percepcao_seguranca_bairro = models.CharField(choices=PERCEPCAO_CHOICES, max_length=1, default=None)
#
#     # problemas_bairro = models.CharField(choices=PROBLEMAS_BAIRRO_CHOICES, max_length=20, default=None, null=True)
#
#     fale_mais_familia = models.CharField('Fale mais sobre sua família',max_length=500)
#
#     class Meta:
#         verbose_name_plural = 'questionários'
#         verbose_name = 'questionário'
#         ordering = ('-criado_em', )
#         unique_together = ['cpf']
#
#     def __str__(self):
#         return self.nome
from sare.questionarios.choices import *


class Questionario(models.Model):
    hashId = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    aluno = models.ForeignKey('core.Aluno', null=True)
    dimensao_economica = models.ForeignKey('DimensaoEconomica', null=True)
    dimensao_social = models.ForeignKey('DimensaoSocial', null=True)
    dimensao_cultural = models.ForeignKey('DimensaoCultural', null=True)
    dimensao_ambiental = models.ForeignKey('DimensaoAmbiental', null=True)
    criado_em = models.DateTimeField('criado em', auto_now_add=True)

    class Meta:
        verbose_name_plural = 'questionários'
        verbose_name = 'questionário'
        ordering = ('-criado_em', )


    def __str__(self):
        return self.aluno.nome


class DimensaoEconomica(models.Model):
    dependentes_RBD = models.IntegerField('Dependentes da Renda Bruta Domiciliar', )
    origem_renda = models.IntegerField('Quantidade de pessoas que possuem renda', )
    renda_bruta_domiciliar = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    responsavel_domicilio = models.CharField(max_length=100)

    # Finanças
    renda_per_capita = models.CharField('Faixa de renda', max_length=1, choices=RENDA_PER_CAPITA_CHOICE, default=None)

    relacao_financeira = models.CharField(choices=DEPENDENCIA_FINANCEIRA_CHOICE,
                                          max_length=1, default=None)

    # Despesas

    despesas_saude_tratamento = models.DecimalField('Tratamento de Saúde', max_digits=8, decimal_places=2, default=0.0)
    despesas_saude_medicamento = models.DecimalField('Medicamentos', max_digits=8, decimal_places=2, default=0.0)
    despesas_saude_cuidador = models.DecimalField('Cuidador de idoso/criança', max_digits=8, decimal_places=2,
                                                  default=0.0)
    despesas_saude_plano = models.DecimalField('Plano de saúde', max_digits=8, decimal_places=2, default=0.0)

    despesas_transporte = models.DecimalField('Transporte', max_digits=8, decimal_places=2, default=0.0)

    despesas_moradia = models.DecimalField('Moradia', max_digits=8, decimal_places=2, default=0.0)

    despesas_educacao_superior = models.DecimalField('Graduação', max_digits=8, decimal_places=2, default=0.0)
    despesas_educacao_basico = models.DecimalField('Ensino Fundamental', max_digits=8, decimal_places=2, default=0.0)
    despesas_educacao_cursinho = models.DecimalField('Cursinhos', max_digits=8, decimal_places=2, default=0.0)
    despesas_educacao_capacitacao = models.DecimalField('Cursos de Capacitação', max_digits=8, decimal_places=2,
                                                        default=0.0)
    despesas_educacao_material = models.DecimalField('Material escolar', max_digits=8, decimal_places=2, default=0.0)

    despesas_bens_fcarro = models.DecimalField('Parcela Carro', max_digits=8, decimal_places=2, default=0.0)
    despesas_bens_fmoto = models.DecimalField('Parcela Moto', max_digits=8, decimal_places=2, default=0.0)
    despesas_bens_terreno = models.DecimalField('Parcela Terreno', max_digits=8, decimal_places=2, default=0.0)

    despesas_domesticas_eletrica = models.DecimalField('Energia elétrica', max_digits=8, decimal_places=2, default=0.0)
    despesas_domesticas_agua = models.DecimalField('Água e esgoto', max_digits=8, decimal_places=2, default=0.0)
    despesas_domesticas_alimentacao = models.DecimalField('Alimentação', max_digits=8, decimal_places=2, default=0.0)

    class Meta:
        verbose_name = 'dimensão econômica'


class DimensaoSocial(models.Model):
    condicao_responsavel_casa = models.CharField(choices=CONDICAO_RESPONSAVEL_CASA_CHOICES, max_length=1, default=None)

    meio_acesso_campus = models.CharField(choices=MEIO_ACESSO_CAMPUS_CHOICES, max_length=1, default=None)

    condicao_moradia = models.CharField(choices=CONDICAO_MORADIA_CHOICES, max_length=2, default=None)

    local_moradia = models.CharField(choices=LOCAL_MORADIA_CHOICES, max_length=1, default=None)

    total_pessoas_casa = models.CharField(choices=TOTAL_PESSOAS_CHOICES, max_length=1, default=None)

    total_comodos_casa = models.CharField(choices=TOTAL_COMODOS_CHOICES, max_length=1, default=None)

    total_km_casa_campus = models.CharField(choices=TOTAL_KM_CHOICES, max_length=1, default=None)

    instituicao_anterior = models.CharField(choices=INSTITUICAO_ANTERIOR_CHOICES, max_length=1, default=None)

    S = ['Faz uso, abuso de bebida alcóolica e/ou drogas?', 'Possui doença grave', 'Possui doença crônica?',
         'Faz uso de medicamento diário, de impacto na renda familiar'
         ]

    saude_bebida_drogas = models.CharField(S[0], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)

    saude_doenca_grave = models.CharField(S[1], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)

    saude_doenca_cronica = models.CharField(S[2], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)

    saude_medicamento_diario = models.CharField(S[3], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)

    PNE = [
        'Tem deficiência parcial de visão/audição?',
        'Possui deficiência física?',
        'Tem deficiência total  de visão/audição?',
        'Tem deficiência mental leve?',
        'Tem deficiência mental grave?',
    ]

    PSI = [
        'Sente dificuldade em se concentrar?',
        'Vivencia algum problema/conflito familiar',
        'Sofre de depressão?',
    ]

    pne_parcial_visao_audicao = models.CharField(PNE[0], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
    pne_def_fisica = models.CharField(PNE[1], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
    pne_total_visao_audicao = models.CharField(PNE[2], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
    pne_def_mental_leve = models.CharField(PNE[3], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
    pne_def_mental_grave = models.CharField(PNE[4], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)

    psico_dificuldade_concentrar = models.CharField(PSI[0], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
    psico_conflito_familiar = models.CharField(PSI[1], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
    psico_depressao = models.CharField(PSI[2], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)

    class Meta:
        verbose_name = 'dimensão social'


class DimensaoCultural(models.Model):

    cor_raca = models.CharField('Como você considera sua cor/raça?', choices=COR_RACA_CHOICES, max_length=1,
                                default=None)

    V = [
        'Verbal(xingamentos, desacatos, etc.)',
        'Violência urbana(assalto, transito, etc)',
        'Patrimonial/financeira',
        'Cyberbulling (por meio de redes sociais)',
        'Religiosa',
        'Assédio Moral',
        'Negligência / abandono familiar',
        'Abuso por parte de familiares ou pessoas conhecidas',
        'Atentado ao pudor',
        'Tráfico de seres humanos',
        'Psicológica / moral',
        'Física',
        'Sexual'
    ]

    violencia_verbal = models.CharField(V[0], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
    violencia_urbana = models.CharField(V[1], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
    violencia_patrimonial = models.CharField(V[2], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
    violencia_cyberbulling = models.CharField(V[3], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
    violencia_religiosa = models.CharField(V[4], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
    violencia_assedio_moral = models.CharField(V[5], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
    violencia_abandono = models.CharField(V[6], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
    violencia_abuso_familiar = models.CharField(V[7], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
    violencia_atentado_pudor = models.CharField(V[8], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
    violencia_trafico_humano = models.CharField(V[9], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
    violencia_psicologica_moral = models.CharField(V[10], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
    violencia_fisica = models.CharField(V[11], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
    violencia_sexual = models.CharField(V[12], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)

    PREC = [
        'Cultural',
        'Estético',
        'Econômico',
        'Religioso',
        'Mental',
        'Racial',
        'Gênero',
        'Orientação sexual'
    ]

    preconceito_cultural = models.CharField(PREC[0], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
    preconceito_estetico = models.CharField(PREC[1], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
    preconceito_economico = models.CharField(PREC[2], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
    preconceito_religioso = models.CharField(PREC[3], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
    preconceito_mental = models.CharField(PREC[4], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
    preconceito_racial = models.CharField(PREC[5], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
    preconceito_genero = models.CharField(PREC[6], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
    preconceito_orientacao_sexual = models.CharField(PREC[7], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)

    class Meta:
        verbose_name = 'dimensão cultural'


class DimensaoAmbiental(models.Model):
    servicos_indisponiveis_bairro = models.CharField(choices=SERVICOS_INDISPONIVEIS_CHOICES, max_length=20, default=None, null=True)
    forma_descarte_lixo = models.CharField(choices=DESCARTE_LIXO_CHOICE, max_length=1, default=None)
    percepcao_seguranca_bairro = models.CharField(choices=PERCEPCAO_CHOICES, max_length=1, default=None)
    problemas_bairro = models.CharField(choices=PROBLEMAS_BAIRRO_CHOICES, max_length=20, default=None, null=True)
    fale_mais_familia = models.CharField('Fale mais sobre sua família', max_length=500)

    class Meta:
        verbose_name = 'dimensão ambiental'
