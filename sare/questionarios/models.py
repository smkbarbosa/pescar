from django.db import models


class Questionario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    SEXO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino')
    )
    sexo = models.CharField(null=True, max_length=1, choices=SEXO_CHOICES)
    cidade = models.CharField(max_length=100)
    bairro = models.CharField(null=True, max_length=100)
    criado_em = models.DateTimeField(auto_now_add=True)

    # Dimensão economica
    dependentes_RBD = models.IntegerField(null=True)
    origem_renda = models.IntegerField(null=True)
    renda_bruta_domiciliar = models.FloatField(null=True)
    responsavel_domicilio = models.CharField(null=True, max_length=100)

    # Finanças
    RENDA_PER_CAPITA_CHOICE = [
        (1, '1.405,51 (a partir)'),
        (2, '937,01 a 1405,50'),
        (3, '468,50 a 937,00'),
        (4, '234,25 até 468,49'),
        (5, 'de 0 até 234, 24')
    ]
    renda_per_capita = models.CharField(null=True, choices=RENDA_PER_CAPITA_CHOICE, max_length=1)

    DEPENDENCIA_FINANCEIRA_CHOICE = [
        (1, 'É independente financeiramente'),
        (2, 'É independente financeiramente e responsável por parte das despesas domésticas'),
        (3, 'É independente totalmente e responsável por todas as despesas domésticas'),
        (4, 'Dependente inteiramente da renda dos pais ou companheiro(s)'),
        (5, 'Dependente inteiramente da renda de outros parentes')
    ]
    relacao_financeira = models.CharField(null=True, choices=DEPENDENCIA_FINANCEIRA_CHOICE,
                                          max_length=1
                                          )

    # Despesas

    despesas_saude_tratamento = models.FloatField(null=True, )
    despesas_saude_medicamento = models.FloatField(null=True, )
    despesas_saude_cuidador = models.FloatField(null=True, )
    despesas_saude_plano = models.FloatField(null=True, )

    despesas_transporte = models.FloatField(null=True, )

    despesas_moradia = models.FloatField(null=True, )

    despesas_educacao_superior = models.FloatField(null=True, )
    despesas_educacao_basico = models.FloatField(null=True, )
    despesas_educacao_cursinho = models.FloatField(null=True, )
    despesas_educacao_capacitacao = models.FloatField(null=True, )
    despesas_educacao_material = models.FloatField(null=True, )

    despesas_bens_fcarro = models.FloatField(null=True, )
    despesas_bens_fmoto = models.FloatField(null=True, )
    despesas_bens_terreno = models.FloatField(null=True, )

    despesas_domesticas_eletrica = models.FloatField(null=True, )
    despesas_domesticas_agua = models.FloatField(null=True, )
    despesas_domesticas_alimentacao = models.FloatField(null=True, )

    # Dimensao Social
    CONDICAO_RESPONSAVEL_CASA_CHOICES = [
        (1, 'Servidor Público'),
        (2, 'Trabalhador contribuinte'),
        (3, 'Trabalhador empregado (CLT)'),
        (4, 'Trabalhador informal (s/ contrib)'),
        (5, 'Desempregado')
    ]
    condicao_responsavel_casa = models.IntegerField(null=True, choices=CONDICAO_RESPONSAVEL_CASA_CHOICES)

    MEIO_ACESSO_CAMPUS_CHOICES = [
        (1, 'Próprio (carro)'),
        (2, 'Próprio (moto)'),
        (3, 'Carona (sem contribuição)'),
        (4, 'Coletivo público (não paga passagem)'),
        (5, 'Vai a pé'),
        (6, 'Vai de bicicleta'),
        (7, 'Carona (com contribuição)'),
        (8, 'Coletivo público (paga passagem)'),
        (9, 'Alternativo (van, etc)')
    ]
    meio_acesso_campus = models.IntegerField(null=True, choices=MEIO_ACESSO_CAMPUS_CHOICES)

    CONDICAO_MORADIA_CHOICES = [
        (1, 'Herança'),
        (2, 'Própria da família (quitada)'),
        (3, 'Própria da família (adquirida por meio de projeto social de habitação, com pagamento de parcelas)'),
        (4, 'Própria da família (financiada)'),
        (5, 'Cedida (gratuita)'),
        (6, 'Própria da família (adquirida por meio de projeto social de habitação, quitada)'),
        (7, 'Alugada'),
        (8, 'Com terceiros (sem contribuição)'),
        (9, 'Com terceiros (com contribuição)'),
        (10, 'Ocupação')
    ]
    condicao_moradia = models.IntegerField(null=True, choices=CONDICAO_MORADIA_CHOICES)

    LOCAL_MORADIA_CHOICES = [
        (1, 'Zona Urbana'),
        (2, 'Zona Rural (fazenda, chácara, sítio)'),
        (3, 'Zona Rural (indígena, quilombola, assentamento)'),
        (4, 'Área de risco (inundação, deslizamento, ocupação, etc)')
    ]
    local_moradia = models.IntegerField(null=True, choices=LOCAL_MORADIA_CHOICES)

    TOTAL_PESSOAS_CHOICES = [
        (1, 'De 1 a 2 pessoas'),
        (2, 'De 3 a 5 pessoas'),
        (3, 'De 6 a 8 pessoas'),
        (4, 'Acima de 9 pessoas')
    ]
    total_pessoas_casa = models.IntegerField(null=True, choices=TOTAL_PESSOAS_CHOICES)

    TOTAL_COMODOS_CHOICES = [
        (1, 'Acima de 9 cômodos'),
        (2, 'De 6 a 8 cômodos'),
        (3, 'De 3 a 5 cômodos'),
        (4, 'De 1 a 2 cômodos')
    ]
    total_comodos_casa = models.IntegerField(null=True, choices=TOTAL_COMODOS_CHOICES)

    TOTAL_KM_CHOICES = [
        (1, '5 km (até)'),
        (2, '6 a 10 km'),
        (3, '11 a 25 km'),
        (4, '26 km (acima de)')
    ]
    total_km_casa_campus = models.IntegerField(null=True, choices=TOTAL_KM_CHOICES)

    INSTITUICAO_ANTERIOR_CHOICES = [
        (1, 'Particular'),
        (2, 'Bolsa total (mérito)'),
        (3, 'Bolsa parcial (mérito)'),
        (4, 'Bolsa parcial (vulnerabilidade)'),
        (5, 'Bolsa total (vulnerabilidade)'),
        (6, 'Pública')
    ]

    instituicao_anterior = models.IntegerField(null=True, choices=INSTITUICAO_ANTERIOR_CHOICES)

    VOCE_FAMILIA_CHOICES = [
        (1, 'Você'),
        (1, 'Família'),
        (1, 'Ambos'),
        (0, 'Não se aplica')
    ]

    SAUDE = ['Faz uso, abuso de bebida alcóolica e/ou drogas?', 'Possui doença grave', 'Possui doença crônica?',
             'Faz uso de medicamento diário, de impacto na renda familiar'
             ]

    saude_bebida_drogas = models.IntegerField(null=True, choices=VOCE_FAMILIA_CHOICES)

    saude_doenca_grave = models.IntegerField(null=True, choices=VOCE_FAMILIA_CHOICES)

    saude_doenca_cronica = models.IntegerField(null=True, choices=VOCE_FAMILIA_CHOICES)

    saude_medicamento_diario = models.IntegerField(null=True, choices=VOCE_FAMILIA_CHOICES)
    PNE = [
        'Tem deficiência parcial de visão/audição?',
        'Possui deficiência física?',
        'Tem deficiência total  de visão/audição?',
        'Tem deficiência mental leve?',
        'Tem deficiência mental grave?',
    ]

    PSICO = [
        'Sente dificuldade em se concentrar?',
        'Vivencia algum problema/conflito familiar',
        'Sofre de depressão?',
    ]

    pne_parcial_visao_audicao = models.IntegerField(null=True, choices=VOCE_FAMILIA_CHOICES)
    pne_def_fisica = models.IntegerField(null=True, choices=VOCE_FAMILIA_CHOICES)
    pne_total_visao_audicao = models.IntegerField(null=True, choices=VOCE_FAMILIA_CHOICES)
    pne_def_mental_leve = models.IntegerField(null=True, choices=VOCE_FAMILIA_CHOICES)
    pne_def_mental_grave = models.IntegerField(null=True, choices=VOCE_FAMILIA_CHOICES)

    psico_dificuldade_concentrar = models.IntegerField(null=True, choices=VOCE_FAMILIA_CHOICES)
    psico_conflito_familiar = models.IntegerField(null=True, choices=VOCE_FAMILIA_CHOICES)
    psico_depressao = models.IntegerField(null=True, choices=VOCE_FAMILIA_CHOICES)

    ## Cultural

    COR_RACA_CHOICES = [
        (1, 'Branca'),
        (2, 'Amarela'),
        (3, 'Parda'),
        (4, 'Estrangeiro'),
        (5, 'Preta'),
        (6, 'Afro descendente Quilombola'),
        (7, 'Indígena'),
        (8, 'Estrangeiro refugiado')
    ]

    cor_raca = models.IntegerField(null=True, choices=COR_RACA_CHOICES)

    VIOLENCIA = [
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

    violencia_verbal = models.IntegerField(null=True, choices=VOCE_FAMILIA_CHOICES)
    violencia_urbana = models.IntegerField(null=True, choices=VOCE_FAMILIA_CHOICES)
    violencia_patrimonial = models.IntegerField(null=True, choices=VOCE_FAMILIA_CHOICES)
    violencia_cyberbulling = models.IntegerField(null=True, choices=VOCE_FAMILIA_CHOICES)
    violencia_religiosa = models.IntegerField(null=True, choices=VOCE_FAMILIA_CHOICES)
    violencia_assedio_moral = models.IntegerField(null=True, choices=VOCE_FAMILIA_CHOICES)
    violencia_abandono = models.IntegerField(null=True, choices=VOCE_FAMILIA_CHOICES)
    violencia_abuso_familiar = models.IntegerField(null=True, choices=VOCE_FAMILIA_CHOICES)
    violencia_atentado_pudor = models.IntegerField(null=True, choices=VOCE_FAMILIA_CHOICES)
    violencia_trafico_humano = models.IntegerField(null=True, choices=VOCE_FAMILIA_CHOICES)
    violencia_psicologica_moral = models.IntegerField(null=True, choices=VOCE_FAMILIA_CHOICES)
    violencia_fisica = models.IntegerField(null=True, choices=VOCE_FAMILIA_CHOICES)
    violencia_sexual = models.IntegerField(null=True, choices=VOCE_FAMILIA_CHOICES)

    PRECONCEITO = [
        'Cultural',
        'Estético',
        'Econômico',
        'Religioso',
        'Mental',
        'Racial',
        'Gênero',
        'Orientação sexual'
    ]

    preconceito_cultural = models.IntegerField(null=True, choices=VOCE_FAMILIA_CHOICES)
    preconceito_estetico = models.IntegerField(null=True, choices=VOCE_FAMILIA_CHOICES)
    preconceito_economico = models.IntegerField(null=True, choices=VOCE_FAMILIA_CHOICES)
    preconceito_religioso = models.IntegerField(null=True, choices=VOCE_FAMILIA_CHOICES)
    preconceito_mental = models.IntegerField(null=True, choices=VOCE_FAMILIA_CHOICES)
    preconceito_racial = models.IntegerField(null=True, choices=VOCE_FAMILIA_CHOICES)
    preconceito_genero = models.IntegerField(null=True, choices=VOCE_FAMILIA_CHOICES)
    preconceito_orientacao_sexual = models.IntegerField(null=True, choices=VOCE_FAMILIA_CHOICES)

    SERVICOS_INDISPONIVEIS_CHOICES = [
        (1, 'Táxi'),
        (2, 'Moto táxi'),
        (3, 'Transporte escolar pago'),
        (4, 'Ônibus escolar'),
        (5, 'Transporte escolar público'),
        (6, 'Ônibus coletivo')
    ]

    servicos_indisponiveis_bairro = models.IntegerField(null=True, choices=SERVICOS_INDISPONIVEIS_CHOICES)

    DESCARTE_LIXO_CHOICE = [
        (1, 'Serviço público de limpeza'),
        (3, 'Jogado em terreno baldio ou em via pública'),
        (2, 'Enterrado'),
        (4, 'Queimado')
    ]

    forma_descarte_lixo = models.IntegerField(null=True, choices=DESCARTE_LIXO_CHOICE)

    PERCEPCAO_CHOICES = [
        (1, 'Não oferece risco de segurança aos seus moradores'),
        (4, 'É considerado perigoso e os moradores sofrem  com a criminalidade'),
        (2, 'Os moradores se sentem seguros (há policiamento nas ruas)'),
        (5, 'Frequentemente os moradores sofrem  algum tipo de violência no bairro ou nos arredores'),
        (3, 'Não há registro de violência sofrida pelo moradores do bairro')
    ]

    percepcao_seguranca_bairro = models.IntegerField(null=True, choices=PERCEPCAO_CHOICES)

    PROBLEMAS_BAIRRO_CHOICES = [
        (1, 'Abastecimento de água'),
        (2, 'Alagamentos'),
        (3, 'Pavimentação (asfalto nas ruas)'),
        (4, 'Energia e iluminação pública'),
        (5, 'Ruas esburacadas (erosão)'),
        (6, 'Saneamento básico (esgoto)'),
        (7, 'Serviços de segurança'),
        (8, 'Acessibilidade '),
        (9, 'Áreas de recreaçao e lazer'),
        (10, 'Limpeza e coleta de lixo'),
        (11, 'Serviços de saúde'),
        (12, 'Transporte público'),
    ]

    problemas_bairro = models.IntegerField(null=True, choices=PROBLEMAS_BAIRRO_CHOICES)

    fale_mais_familia = models.CharField(null=True, max_length=500)