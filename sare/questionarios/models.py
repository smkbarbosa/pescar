import uuid

from django.db import models

from sare.questionarios.validators import validate_cpf

SEXO_CHOICES = (
    ('M', 'Masculino'),
    ('F', 'Feminino')
)

DEPENDENCIA_FINANCEIRA_CHOICE = (
    ('1', 'É independente financeiramente'),
    ('2', 'É independente financeiramente e responsável por parte das despesas domésticas'),
    ('3', 'É independente totalmente e responsável por todas as despesas domésticas'),
    ('4', 'Dependente inteiramente da renda dos pais ou companheiro(s)'),
    ('5', 'Dependente inteiramente da renda de outros parentes')
)

RENDA_PER_CAPITA_CHOICE = (
    ('1', '1.431,01 (a partir)'),
    ('2', '954,01 a 1431,00'),
    ('3', '477,01 a 954,00'),
    ('4', '238,50 até 477,00'),
    ('5', 'de 0 até 238, 49')
)

CONDICAO_RESPONSAVEL_CASA_CHOICES = (
    ('1', 'Servidor Público'),
    ('2', 'Trabalhador contribuinte'),
    ('3', 'Trabalhador empregado (CLT)'),
    ('4', 'Trabalhador informal (s/ contrib)'),
    ('5', 'Desempregado')
)


MEIO_ACESSO_CAMPUS_CHOICES = (
    ('1', 'Próprio (carro)'),
    ('2', 'Próprio (moto)'),
    ('3', 'Carona (sem contribuição)'),
    ('4', 'Coletivo público (não paga passagem)'),
    ('5', 'Vai a pé'),
    ('6', 'Vai de bicicleta'),
    ('7', 'Carona (com contribuição)'),
    ('8', 'Coletivo público (paga passagem)'),
    ('9', 'Alternativo (van, etc)')
)

CONDICAO_MORADIA_CHOICES = (
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
)

LOCAL_MORADIA_CHOICES = (
    ('1', 'Zona Urbana'),
    ('2', 'Zona Rural (fazenda, chácara, sítio)'),
    ('3', 'Zona Rural (indígena, quilombola, assentamento)'),
    ('4', 'Área de risco (inundação, deslizamento, ocupação, etc)')
)

TOTAL_PESSOAS_CHOICES = (
    ('1', 'De 1 a 2 pessoas'),
    ('2', 'De 3 a 5 pessoas'),
    ('3', 'De 6 a 8 pessoas'),
    ('4', 'Acima de 9 pessoas')
)

TOTAL_KM_CHOICES = (
    ('1', '5 km (até)'),
    ('2', '6 a 10 km'),
    ('3', '11 a 25 km'),
    ('4', '26 km (acima de)')
)

TOTAL_COMODOS_CHOICES = (
    ('1', 'Acima de 9 cômodos'),
    ('2', 'De 6 a 8 cômodos'),
    ('3', 'De 3 a 5 cômodos'),
    ('4', 'De 1 a 2 cômodos')
)

INSTITUICAO_ANTERIOR_CHOICES = (
    ('1', 'Particular'),
    ('2', 'Bolsa total (mérito)'),
    ('3', 'Bolsa parcial (mérito)'),
    ('4', 'Bolsa parcial (vulnerabilidade)'),
    ('5', 'Bolsa total (vulnerabilidade)'),
    ('6', 'Pública')
)

VOCE_FAMILIA_CHOICES = (
    ('1', 'Você'),
    ('2', 'Família'),
    ('3', 'Ambos'),
    ('0', 'Não se aplica')
)

SERVICOS_INDISPONIVEIS_CHOICES = (
    ('1', 'Táxi'),
    ('2', 'Moto táxi'),
    ('3', 'Transporte escolar pago'),
    ('4', 'Ônibus escolar'),
    ('5', 'Transporte escolar público'),
    ('6', 'Ônibus coletivo')
)

COR_RACA_CHOICES = (
        ('1', 'Branca'),
        ('2', 'Amarela'),
        ('3', 'Parda'),
        ('4', 'Estrangeiro'),
        ('5', 'Preta'),
        ('6', 'Afro descendente Quilombola'),
        ('7', 'Indígena'),
        ('8', 'Estrangeiro refugiado')
    )

PERCEPCAO_CHOICES = (
    ('1', 'Não oferece risco de segurança aos seus moradores'),
    ('4', 'É considerado perigoso e os moradores sofrem  com a criminalidade'),
    ('2', 'Os moradores se sentem seguros (há policiamento nas ruas)'),
    ('5', 'Frequentemente os moradores sofrem  algum tipo de violência no bairro ou nos arredores'),
    ('3', 'Não há registro de violência sofrida pelo moradores do bairro')
)

PROBLEMAS_BAIRRO_CHOICES = (
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
)

DESCARTE_LIXO_CHOICE = (
    ('1', 'Serviço público de limpeza'),
    ('3', 'Jogado em terreno baldio ou em via pública'),
    ('2', 'Enterrado'),
    ('4', 'Queimado')
)

CURSO_CHOICE = (
    ('1', 'PROEJA - ATENDIMENTO'),
    ('2', 'PROEJA - MANUTENÇÃO E OPERAÇÃO DE MICROCOMPUTADORESs'),
    ('3', 'TEC. INT. - TÉCNICO EM ADMINISTRAÇÃO'),
    ('4', 'TEC. INT. - TÉCNICO EM AGRIMENSURA'),
    ('5', 'TEC. INT. - TÉCNICO EM AGRONEGÓCIO'),
    ('6', 'TEC. INT. - TÉCNICO EM CONTROLE AMBIENTAL '),
    ('7', 'TEC. INT. - TÉCNICO EM ELETROTÉCNICA'),
    ('8', 'TEC. INT. - TÉCNICO EM EVENTOS'),
    ('9', 'TEC. INT. - TÉCNICO EM INFORMÁTICA PARA INTERNET'),
    ('10', 'TEC. INT. - TÉCNICO EM MECATRÔNICA'),
    ('11', 'TEC. SUB. - TÉCNICO EM AGRIMENSURA'),
    ('12', 'TEC. SUB. - TÉCNICO EM AUTOMAÇÃO INDUSTRIAL'),
    ('13', 'TEC. SUB. - TÉCNICO EM EDIFICAÇÕES'),
    ('14', 'TEC. SUB. - TÉCNICO EM ELETROTÉCNICA'),
    ('15', 'TEC. SUB. - TÉCNICO EM INFORMÁTICA'),
    ('16', 'TEC. SUB. - TÉCNICO EM SECRETARIADO'),
    ('17', 'TEC. SUB. - TÉCNICO EM SEGURANÇA DO TRABALHO'),
    ('18', 'GRADUAÇÃO - ENGENHARIA CIVIL'),
    ('19', 'GRADUAÇÃO - ENGENHARIA ELÉTRICA'),
    ('20', 'GRADUAÇÃO - EDUCAÇÃO FÍSICA'),
    ('21', 'GRADUAÇÃO - FÍSICA'),
    ('22', 'GRADUAÇÃO - LETRAS - LÍNGUA PORTUGUESA'),
    ('23', 'GRADUAÇÃO - MATEMÁTICA'),
    ('24', 'GRADUAÇÃO - AGRONEGÓCIO'),
    ('25', 'GRADUAÇÃO - CONSTRUÇÃO DE EDIFÍCIOS'),
    ('26', 'GRADUAÇÃO - GESTÃO DE TURISMO'),
    ('27', 'GRADUAÇÃO - GESTÃO PÚBLICA'),
    ('28', 'GRADUAÇÃO - SISTEMAS ELÉTRICOS'),
    ('29', 'GRADUAÇÃO - SISTEMAS PARA INTERNET')
)


class Questionario(models.Model):
    hashId = models.UUIDField(primary_key=False, default=uuid.uuid4, editable=False)
    nome = models.CharField('nome', max_length=100)
    cpf = models.CharField('CPF', max_length=11, validators=[validate_cpf])
    email = models.EmailField('e-mail')
    fone = models.CharField('telefone',max_length=20, blank=True)

    endereco = models.CharField('endereço', max_length=100, default=None)
    num_casa = models.CharField('número da casa', max_length=4, default=0)
    cep = models.CharField('cep', max_length=9, default=None)
    bairro = models.CharField('bairro', max_length=100)
    cidade = models.CharField('cidade', max_length=100)
    estado = models.CharField('estado', max_length=2, default='TO')
    sexo = models.CharField('sexo', max_length=1, choices=SEXO_CHOICES, default=None)

    curso = models.CharField('curso', choices=CURSO_CHOICE, max_length=50, blank=True)
    sem_mod_ano = models.CharField('Semestre/Módulo/Ano', max_length=10, default=None)
    matricula = models.CharField('matrícula', max_length=15, default=None)
    campus = models.CharField('campus', max_length=30, default='PALMAS')

    criado_em = models.DateTimeField('criado em', auto_now_add=True)

    # Dimensão economica
    dependentes_RBD = models.IntegerField('Dependentes da Renda Bruta Domiciliar', )
    origem_renda = models.IntegerField('Quantidade de pessoas que possuem renda',)
    renda_bruta_domiciliar = models.DecimalField(max_digits=8, decimal_places=2)
    responsavel_domicilio = models.CharField(max_length=100)

    # Finanças
    renda_per_capita = models.CharField('Faixa de renda', max_length=1, choices=RENDA_PER_CAPITA_CHOICE, default=None)

    relacao_financeira = models.CharField(choices=DEPENDENCIA_FINANCEIRA_CHOICE,
                                          max_length=1, default=None)

    # Despesas

    despesas_saude_tratamento = models.DecimalField('Tratamento de Saúde', max_digits=8, decimal_places=2)
    despesas_saude_medicamento = models.DecimalField('Medicamentos', max_digits=8, decimal_places=2)
    despesas_saude_cuidador = models.DecimalField('Cuidador de idoso/criança', max_digits=8, decimal_places=2)
    despesas_saude_plano = models.DecimalField('Plano de saúde', max_digits=8, decimal_places=2)

    despesas_transporte = models.DecimalField('Transporte', max_digits=8, decimal_places=2)

    despesas_moradia = models.DecimalField('Moradia', max_digits=8, decimal_places=2)

    despesas_educacao_superior = models.DecimalField('Graduação', max_digits=8, decimal_places=2)
    despesas_educacao_basico = models.DecimalField('Ensino Fundamental', max_digits=8, decimal_places=2)
    despesas_educacao_cursinho = models.DecimalField('Cursinhos', max_digits=8, decimal_places=2)
    despesas_educacao_capacitacao = models.DecimalField('Cursos de Capacitação', max_digits=8, decimal_places=2)
    despesas_educacao_material = models.DecimalField('Material escolar', max_digits=8, decimal_places=2)

    despesas_bens_fcarro = models.DecimalField('Parcela Carro', max_digits=8, decimal_places=2)
    despesas_bens_fmoto = models.DecimalField('Parcela Moto', max_digits=8, decimal_places=2)
    despesas_bens_terreno = models.DecimalField('Parcela Terreno', max_digits=8, decimal_places=2)

    despesas_domesticas_eletrica = models.DecimalField('Energia elétrica', max_digits=8, decimal_places=2)
    despesas_domesticas_agua = models.DecimalField('Água e esgoto', max_digits=8, decimal_places=2)
    despesas_domesticas_alimentacao = models.DecimalField('Alimentação', max_digits=8, decimal_places=2)

    # Dimensao Social
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

    pne_parcial_visao_audicao = models.CharField(PNE[0],choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
    pne_def_fisica = models.CharField(PNE[1], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
    pne_total_visao_audicao = models.CharField(PNE[2], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
    pne_def_mental_leve = models.CharField(PNE[3], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
    pne_def_mental_grave = models.CharField(PNE[4], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)

    psico_dificuldade_concentrar = models.CharField(PSI[0], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
    psico_conflito_familiar = models.CharField(PSI[1], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)
    psico_depressao = models.CharField(PSI[2], choices=VOCE_FAMILIA_CHOICES, max_length=1, default=None)

    ## Cultural

    cor_raca = models.CharField('Como você considera sua cor/raça?', choices=COR_RACA_CHOICES, max_length=1, default=None)

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

    # servicos_indisponiveis_bairro = models.CharField(choices=SERVICOS_INDISPONIVEIS_CHOICES, max_length=20, default=None, null=True)

    forma_descarte_lixo = models.CharField(choices=DESCARTE_LIXO_CHOICE, max_length=1, default=None)

    percepcao_seguranca_bairro = models.CharField(choices=PERCEPCAO_CHOICES, max_length=1, default=None)

    # problemas_bairro = models.CharField(choices=PROBLEMAS_BAIRRO_CHOICES, max_length=20, default=None, null=True)

    fale_mais_familia = models.CharField('Fale mais sobre sua família',max_length=500)

    class Meta:
        verbose_name_plural = 'questionários'
        verbose_name = 'questionário'
        ordering = ('-criado_em', )

    def __str__(self):
        return self.nome
