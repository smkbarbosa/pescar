from collections import OrderedDict


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

CURSO_CHOICE = OrderedDict((
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
    ('30', 'TEC. SUB. - TÉCNICO EM CONTROLE AMBIENTAL'),
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
))
