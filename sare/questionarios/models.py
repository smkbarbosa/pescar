import uuid

from django.db import models

from sare.questionarios.validators import validate_cpf

SEXO_CHOICES = (
    ('M', 'Masculino'),
    ('F', 'Feminino')
)

DEPENDENCIA_FINANCEIRA_CHOICE = (
    (1, 'É independente financeiramente'),
    (2, 'É independente financeiramente e responsável por parte das despesas domésticas'),
    (3, 'É independente totalmente e responsável por todas as despesas domésticas'),
    (4, 'Dependente inteiramente da renda dos pais ou companheiro(s)'),
    (5, 'Dependente inteiramente da renda de outros parentes')
)


class Questionario(models.Model):
    hashId = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    nome = models.CharField('nome', max_length=100)
    cpf = models.CharField('CPF', max_length=11, validators=[validate_cpf])
    email = models.EmailField('e-mail')

    bairro = models.CharField('bairro', blank=True, max_length=100)
    cidade = models.CharField('cidade', max_length=100)
    sexo = models.CharField('sexo', max_length=1, choices=SEXO_CHOICES)

    criado_em = models.DateTimeField('criado em', auto_now_add=True)

    # Dimensão economica
    dependentes_RBD = models.IntegerField('Dependentes da Renda Bruta Domiciliar', blank=True)
    origem_renda = models.IntegerField('Quantidade de pessoas que possuem renda',blank=True)
    renda_bruta_domiciliar = models.FloatField(blank=True)
    responsavel_domicilio = models.CharField(blank=True, max_length=100)

    # Finanças
    RENDA_PER_CAPITA_CHOICE = [
        (1, '1.405,51 (a partir)'),
        (2, '937,01 a 1405,50'),
        (3, '468,50 a 937,00'),
        (4, '234,25 até 468,49'),
        (5, 'de 0 até 234, 24')
    ]
    renda_per_capita = models.CharField('Faixa de renda', blank=True, max_length=1, choices=RENDA_PER_CAPITA_CHOICE)

    relacao_financeira = models.CharField(choices=DEPENDENCIA_FINANCEIRA_CHOICE,
                                          max_length=1, blank=True)

    # Despesas

    despesas_saude_tratamento = models.FloatField('Tratamento de Saúde',blank=True, )
    despesas_saude_medicamento = models.FloatField('Medicamentos', blank=True, )
    despesas_saude_cuidador = models.FloatField('Cuidador de idoso/criança', blank=True, )
    despesas_saude_plano = models.FloatField('Plano de saúde', blank=True, )

    despesas_transporte = models.FloatField('Transporte', blank=True, )

    despesas_moradia = models.FloatField('Moradia', blank=True, )

    despesas_educacao_superior = models.FloatField('Graduação', blank=True, )
    despesas_educacao_basico = models.FloatField('Ensino Fundamental', blank=True, )
    despesas_educacao_cursinho = models.FloatField('Cursinhos', blank=True, )
    despesas_educacao_capacitacao = models.FloatField('Cursos de Capacitação', blank=True, )
    despesas_educacao_material = models.FloatField('Material escolar', blank=True, )

    despesas_bens_fcarro = models.FloatField('Parcela Carro', blank=True, )
    despesas_bens_fmoto = models.FloatField('Parcela Moto', blank=True, )
    despesas_bens_terreno = models.FloatField('Parcela Terreno', blank=True, )

    despesas_domesticas_eletrica = models.FloatField('Energia elétrica', blank=True, )
    despesas_domesticas_agua = models.FloatField('Água e esgoto', blank=True, )
    despesas_domesticas_alimentacao = models.FloatField('Alimentação', blank=True, )

    # Dimensao Social
    CONDICAO_RESPONSAVEL_CASA_CHOICES = [
        ('1', 'Servidor Público'),
        ('2', 'Trabalhador contribuinte'),
        ('3', 'Trabalhador empregado (CLT)'),
        ('4', 'Trabalhador informal (s/ contrib)'),
        ('5', 'Desempregado')
    ]
    condicao_responsavel_casa = models.CharField(blank=True, choices=CONDICAO_RESPONSAVEL_CASA_CHOICES, max_length=1)

    MEIO_ACESSO_CAMPUS_CHOICES = [
        ('1', 'Próprio (carro)'),
        ('2', 'Próprio (moto)'),
        ('3', 'Carona (sem contribuição)'),
        ('4', 'Coletivo público (não paga passagem)'),
        ('5', 'Vai a pé'),
        ('6', 'Vai de bicicleta'),
        ('7', 'Carona (com contribuição)'),
        ('8', 'Coletivo público (paga passagem)'),
        ('9', 'Alternativo (van, etc)')
    ]
    meio_acesso_campus = models.CharField(blank=True, choices=MEIO_ACESSO_CAMPUS_CHOICES, max_length=1)

    CONDICAO_MORADIA_CHOICES = [
        ('1', 'Herança'),
        ('2', 'Própria da família (quitada)'),
        ('3', 'Própria da família (adquirida por meio de projeto social de habitação, com pagamento de parcelas)'),
        ('4', 'Própria da família (financiada)'),
        ('5', 'Cedida (gratuita)'),
        ('6', 'Própria da família (adquirida por meio de projeto social de habitação, quitada)'),
        ('7', 'Alugada'),
        ('8', 'Com terceiros (sem contribuição)'),
        ('9', 'Com terceiros (com contribuição)'),
        ('10', 'Ocupação')
    ]
    condicao_moradia = models.CharField(blank=True, choices=CONDICAO_MORADIA_CHOICES, max_length=2)

    LOCAL_MORADIA_CHOICES = [
        ('1', 'Zona Urbana'),
        ('2', 'Zona Rural (fazenda, chácara, sítio)'),
        ('3', 'Zona Rural (indígena, quilombola, assentamento)'),
        ('4', 'Área de risco (inundação, deslizamento, ocupação, etc)')
    ]
    local_moradia = models.CharField(blank=True, choices=LOCAL_MORADIA_CHOICES, max_length=1)

    TOTAL_PESSOAS_CHOICES = [
        ('1', 'De 1 a 2 pessoas'),
        ('2', 'De 3 a 5 pessoas'),
        ('3', 'De 6 a 8 pessoas'),
        ('4', 'Acima de 9 pessoas')
    ]
    total_pessoas_casa = models.CharField(blank=True, choices=TOTAL_PESSOAS_CHOICES, max_length=1)

    TOTAL_COMODOS_CHOICES = [
        ('1', 'Acima de 9 cômodos'),
        ('2', 'De 6 a 8 cômodos'),
        ('3', 'De 3 a 5 cômodos'),
        ('4', 'De 1 a 2 cômodos')
    ]
    total_comodos_casa = models.CharField(blank=True, choices=TOTAL_COMODOS_CHOICES, max_length=1)

    TOTAL_KM_CHOICES = [
        ('1', '5 km (até)'),
        ('2', '6 a 10 km'),
        ('3', '11 a 25 km'),
        ('4', '26 km (acima de)')
    ]
    total_km_casa_campus = models.CharField(blank=True, choices=TOTAL_KM_CHOICES, max_length=1)

    INSTITUICAO_ANTERIOR_CHOICES = [
        ('1', 'Particular'),
        ('2', 'Bolsa total (mérito)'),
        ('3', 'Bolsa parcial (mérito)'),
        ('4', 'Bolsa parcial (vulnerabilidade)'),
        ('5', 'Bolsa total (vulnerabilidade)'),
        ('6', 'Pública')
    ]

    instituicao_anterior = models.CharField(blank=True, choices=INSTITUICAO_ANTERIOR_CHOICES, max_length=1)

    VOCE_FAMILIA_CHOICES = [
        ('1', 'Você'),
        ('2', 'Família'),
        ('3', 'Ambos'),
        ('0', 'Não se aplica')
    ]

    S = ['Faz uso, abuso de bebida alcóolica e/ou drogas?', 'Possui doença grave', 'Possui doença crônica?',
             'Faz uso de medicamento diário, de impacto na renda familiar'
             ]

    saude_bebida_drogas = models.CharField(S[0], blank=True, choices=VOCE_FAMILIA_CHOICES, max_length=1)

    saude_doenca_grave = models.CharField(S[1], blank=True, choices=VOCE_FAMILIA_CHOICES, max_length=1)

    saude_doenca_cronica = models.CharField(S[2], blank=True, choices=VOCE_FAMILIA_CHOICES, max_length=1)

    saude_medicamento_diario = models.CharField(S[3], blank=True, choices=VOCE_FAMILIA_CHOICES, max_length=1)

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

    pne_parcial_visao_audicao = models.CharField(PNE[0],blank=True, choices=VOCE_FAMILIA_CHOICES, max_length=1)
    pne_def_fisica = models.CharField(PNE[1], blank=True, choices=VOCE_FAMILIA_CHOICES, max_length=1)
    pne_total_visao_audicao = models.CharField(PNE[2], blank=True, choices=VOCE_FAMILIA_CHOICES, max_length=1)
    pne_def_mental_leve = models.CharField(PNE[3], blank=True, choices=VOCE_FAMILIA_CHOICES, max_length=1)
    pne_def_mental_grave = models.CharField(PNE[4], blank=True, choices=VOCE_FAMILIA_CHOICES, max_length=1)

    psico_dificuldade_concentrar = models.CharField(PSI[0], blank=True, choices=VOCE_FAMILIA_CHOICES, max_length=1)
    psico_conflito_familiar = models.CharField(PSI[1], blank=True, choices=VOCE_FAMILIA_CHOICES, max_length=1)
    psico_depressao = models.CharField(PSI[2], blank=True, choices=VOCE_FAMILIA_CHOICES, max_length=1)

    ## Cultural

    COR_RACA_CHOICES = [
        ('1', 'Branca'),
        ('2', 'Amarela'),
        ('3', 'Parda'),
        ('4', 'Estrangeiro'),
        ('5', 'Preta'),
        ('6', 'Afro descendente Quilombola'),
        ('7', 'Indígena'),
        ('8', 'Estrangeiro refugiado')
    ]

    cor_raca = models.CharField('Como você considera sua cor/raça?', blank=True, choices=COR_RACA_CHOICES, max_length=1)

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

    violencia_verbal = models.CharField(V[0], blank=True, choices=VOCE_FAMILIA_CHOICES, max_length=1)
    violencia_urbana = models.CharField(V[1], blank=True, choices=VOCE_FAMILIA_CHOICES, max_length=1)
    violencia_patrimonial = models.CharField(V[2], blank=True, choices=VOCE_FAMILIA_CHOICES, max_length=1)
    violencia_cyberbulling = models.CharField(V[3], blank=True, choices=VOCE_FAMILIA_CHOICES, max_length=1)
    violencia_religiosa = models.CharField(V[4], blank=True, choices=VOCE_FAMILIA_CHOICES, max_length=1)
    violencia_assedio_moral = models.CharField(V[5], blank=True, choices=VOCE_FAMILIA_CHOICES, max_length=1)
    violencia_abandono = models.CharField(V[6], blank=True, choices=VOCE_FAMILIA_CHOICES, max_length=1)
    violencia_abuso_familiar = models.CharField(V[7], blank=True, choices=VOCE_FAMILIA_CHOICES, max_length=1)
    violencia_atentado_pudor = models.CharField(V[8], blank=True, choices=VOCE_FAMILIA_CHOICES, max_length=1)
    violencia_trafico_humano = models.CharField(V[9], blank=True, choices=VOCE_FAMILIA_CHOICES, max_length=1)
    violencia_psicologica_moral = models.CharField(V[10], blank=True, choices=VOCE_FAMILIA_CHOICES, max_length=1)
    violencia_fisica = models.CharField(V[11], blank=True, choices=VOCE_FAMILIA_CHOICES, max_length=1)
    violencia_sexual = models.CharField(V[12], blank=True, choices=VOCE_FAMILIA_CHOICES, max_length=1)

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

    preconceito_cultural = models.CharField(PREC[0], blank=True, choices=VOCE_FAMILIA_CHOICES, max_length=1)
    preconceito_estetico = models.CharField(PREC[1], blank=True, choices=VOCE_FAMILIA_CHOICES, max_length=1)
    preconceito_economico = models.CharField(PREC[2], blank=True, choices=VOCE_FAMILIA_CHOICES, max_length=1)
    preconceito_religioso = models.CharField(PREC[3], blank=True, choices=VOCE_FAMILIA_CHOICES, max_length=1)
    preconceito_mental = models.CharField(PREC[4], blank=True, choices=VOCE_FAMILIA_CHOICES, max_length=1)
    preconceito_racial = models.CharField(PREC[5], blank=True, choices=VOCE_FAMILIA_CHOICES, max_length=1)
    preconceito_genero = models.CharField(PREC[6], blank=True, choices=VOCE_FAMILIA_CHOICES, max_length=1)
    preconceito_orientacao_sexual = models.CharField(PREC[7], blank=True, choices=VOCE_FAMILIA_CHOICES, max_length=1)

    SERVICOS_INDISPONIVEIS_CHOICES = [
        ('1', 'Táxi'),
        ('2', 'Moto táxi'),
        ('3', 'Transporte escolar pago'),
        ('4', 'Ônibus escolar'),
        ('5', 'Transporte escolar público'),
        ('6', 'Ônibus coletivo')
    ]

    servicos_indisponiveis_bairro = models.CharField(blank=True, choices=SERVICOS_INDISPONIVEIS_CHOICES, max_length=1)

    DESCARTE_LIXO_CHOICE = [
        ('1', 'Serviço público de limpeza'),
        ('3', 'Jogado em terreno baldio ou em via pública'),
        ('2', 'Enterrado'),
        ('4', 'Queimado')
    ]

    forma_descarte_lixo = models.CharField(blank=True, choices=DESCARTE_LIXO_CHOICE, max_length=1)

    PERCEPCAO_CHOICES = [
        ('1', 'Não oferece risco de segurança aos seus moradores'),
        ('4', 'É considerado perigoso e os moradores sofrem  com a criminalidade'),
        ('2', 'Os moradores se sentem seguros (há policiamento nas ruas)'),
        ('5', 'Frequentemente os moradores sofrem  algum tipo de violência no bairro ou nos arredores'),
        ('3', 'Não há registro de violência sofrida pelo moradores do bairro')
    ]

    percepcao_seguranca_bairro = models.CharField(blank=True, choices=PERCEPCAO_CHOICES, max_length=1)

    PROBLEMAS_BAIRRO_CHOICES = [
        ('1', 'Abastecimento de água'),
        ('2', 'Alagamentos'),
        ('3', 'Pavimentação (asfalto nas ruas)'),
        ('4', 'Energia e iluminação pública'),
        ('5', 'Ruas esburacadas (erosão)'),
        ('6', 'Saneamento básico (esgoto)'),
        ('7', 'Serviços de segurança'),
        ('8', 'Acessibilidade '),
        ('9', 'Áreas de recreaçao e lazer'),
        ('10', 'Limpeza e coleta de lixo'),
        ('11', 'Serviços de saúde'),
        ('12', 'Transporte público'),
    ]

    problemas_bairro = models.CharField(blank=True, choices=PROBLEMAS_BAIRRO_CHOICES, max_length=2)

    fale_mais_familia = models.CharField('Fale mais sobre sua família',blank=True, max_length=500)


    class Meta:
        verbose_name_plural = 'questionários'
        verbose_name = 'questionário'
        ordering = ('-criado_em', )

    def __str__(self):
        return self.nome