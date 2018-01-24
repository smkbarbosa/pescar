from django import forms
from material import *


class QuestionarioForm(forms.Form):

    # Dados Pessoais
    nome = forms.CharField(label='Nome')
    cpf = forms.CharField(label='CPF')
    email = forms.EmailField(label='E-mail')
    # bairro = forms.CharField(label='Bairro')
    cidade = forms.CharField(label='Cidade')

    # sexo = forms.ChoiceField(choices=(('M', 'Masculino'),('F', 'Feminino')),
    #                          widget=forms.RadioSelect, label='Sexo')


    # Dimensão: Economica
    # dependentes_RBD = forms.IntegerField(label='Quantidade de dependentes da Renda Bruta Domiciliar (RBD)')
    # origem_renda = forms.IntegerField(label='Origem da renda')
    # renda_bruta_domiciliar = forms.FloatField(label='Renda Bruta Domiciliar')
    # responsavel_domicilio = forms.CharField(label="Responsável pela manutenção do domicílio")

    # # Finanças
    # RENDA_PER_CAPITA_CHOICE = [
    #     (1, '1.405,51 (a partir)'),
    #     (2, '937,01 a 1405,50'),
    #     (3, '468,50 a 937,00'),
    #     (4, '234,25 até 468,49'),
    #     (5, 'de 0 até 234, 24')
    # ]
    # renda_per_capita = forms.ChoiceField(choices=RENDA_PER_CAPITA_CHOICE, widget=forms.RadioSelect,
    #                                      label='Renda per capita domiciliar')
    #
    # DEPENDENCIA_FINANCEIRA_CHOICE = [
    #     (1, 'É independente financeiramente'),
    #     (2, 'É independente financeiramente e responsável por parte das despesas domésticas'),
    #     (3, 'É independente totalmente e responsável por todas as despesas domésticas'),
    #     (4, 'Dependente inteiramente da renda dos pais ou companheiro(s)'),
    #     (5, 'Dependente inteiramente da renda de outros parentes')
    # ]
    # relacao_financeira = forms.ChoiceField(choices=DEPENDENCIA_FINANCEIRA_CHOICE, widget=forms.RadioSelect,
    #                                        label='Qual é a sua relação financeira?')
    #
    # # Despesas
    #
    # despesas_saude_tratamento = forms.CharField(label='Tratamento de saúde (a partir de R$ 234,24)')
    # despesas_saude_medicamento = forms.CharField(label='Medicamentos (a partir de R$ 200,00)')
    # despesas_saude_cuidador = forms.CharField(label='Cuidador de idoso/criança/PNE')
    # despesas_saude_plano = forms.CharField(label='Plano de Saúde')
    #
    # despesas_transporte = forms.CharField(label='Transporte para acessar o Campus')
    #
    # despesas_moradia = forms.CharField(label='Aluguel/Financiamento')
    #
    # despesas_educacao_superior = forms.CharField(label='Educação Superior')
    # despesas_educacao_basico = forms.CharField(label='Educação Básica (Fundamental e Médio')
    # despesas_educacao_cursinho = forms.CharField(label='Curso Preparatório (cursinhos, etc)')
    # despesas_educacao_capacitacao = forms.CharField(label='Curso de Capacitação')
    # despesas_educacao_material = forms.CharField(label='Material Didático')
    #
    # despesas_bens_fcarro = forms.CharField(label='Financiamento de carro (até R$ 800,00/mês)')
    # despesas_bens_fmoto = forms.CharField(label='Financiamento de moto (até R$ 300,00/mês')
    # despesas_bens_terreno = forms.CharField(label='Terreno/Lote (até R$ 600,00/mês')
    #
    # despesas_domesticas_eletrica = forms.CharField(label='Energia (até R$ 200,00/mês)')
    # despesas_domesticas_agua = forms.CharField(label='Água (até R$ 150,00/mês')
    # despesas_domesticas_alimentacao = forms.CharField(label='Alimentação (até R$ 650,00/mês')
    #
    # # Dimensao Social
    # CONDICAO_RESPONSAVEL_CASA_CHOICES = [
    #     (1, 'Servidor Público'),
    #     (2, 'Trabalhador contribuinte'),
    #     (3, 'Trabalhador empregado (CLT)'),
    #     (4, 'Trabalhador informal (s/ contrib)'),
    #     (5, 'Desempregado')
    # ]
    # condicao_responsavel_casa = forms.ChoiceField(choices=CONDICAO_RESPONSAVEL_CASA_CHOICES, widget=forms.RadioSelect,
    #                                               label='Informe a sua condição de trabalho ou do principal '
    #                                                     'responsável pela manutenção da casa')
    #
    # MEIO_ACESSO_CAMPUS_CHOICES = [
    #     (1, 'Próprio (carro)'),
    #     (2, 'Próprio (moto)'),
    #     (3, 'Carona (sem contribuição)'),
    #     (4, 'Coletivo público (não paga passagem)'),
    #     (5, 'Vai a pé'),
    #     (6, 'Vai de bicicleta'),
    #     (7, 'Carona (com contribuição)'),
    #     (8, 'Coletivo público (paga passagem)'),
    #     (9, 'Alternativo (van, etc)')
    # ]
    # meio_acesso_campus = forms.ChoiceField(choices=MEIO_ACESSO_CAMPUS_CHOICES, widget=forms.RadioSelect,
    #                                        label='Meio de acesso ao Campus')
    #
    # CONDICAO_MORADIA_CHOICES = [
    #     (1, 'Herança'),
    #     (2, 'Própria da família (quitada)'),
    #     (3, 'Própria da família (adquirida por meio de projeto social de habitação, com pagamento de parcelas)'),
    #     (4, 'Própria da família (financiada)'),
    #     (5, 'Cedida (gratuita)'),
    #     (6, 'Própria da família (adquirida por meio de projeto social de habitação, quitada)'),
    #     (7, 'Alugada'),
    #     (8, 'Com terceiros (sem contribuição)'),
    #     (9, 'Com terceiros (com contribuição)'),
    #     (10, 'Ocupação')
    # ]
    # condicao_moradia = forms.ChoiceField(CONDICAO_MORADIA_CHOICES, widget=forms.RadioSelect,
    #                                      label='Condição da Moradia')
    #
    # LOCAL_MORADIA_CHOICES = [
    #     (1, 'Zona Urbana'),
    #     (2, 'Zona Rural (fazenda, chácara, sítio)'),
    #     (3, 'Zona Rural (indígena, quilombola, assentamento)'),
    #     (4, 'Área de risco (inundação, deslizamento, ocupação, etc)')
    # ]
    # local_moradia = forms.ChoiceField(choices=LOCAL_MORADIA_CHOICES, widget=forms.RadioSelect,
    #                                   label='Local de Moradia')
    #
    # TOTAL_PESSOAS_CHOICES = [
    #     (1, 'De 1 a 2 pessoas'),
    #     (2, 'De 3 a 5 pessoas'),
    #     (3, 'De 6 a 8 pessoas'),
    #     (4, 'Acima de 9 pessoas')
    # ]
    # total_pessoas_casa = forms.ChoiceField(choices=TOTAL_PESSOAS_CHOICES, widget=forms.RadioSelect,
    #                                        label='Incluindo você, quantas pessoas moram na casa?')
    #
    # TOTAL_COMODOS_CHOICES = [
    #     (1, 'Acima de 9 cômodos'),
    #     (2, 'De 6 a 8 cômodos'),
    #     (3, 'De 3 a 5 cômodos'),
    #     (4, 'De 1 a 2 cômodos')
    # ]
    # total_comodos_casa = forms.ChoiceField(choices=TOTAL_COMODOS_CHOICES, widget=forms.RadioSelect,
    #                                        label='Incluindo banheiros, quantos cômodos tem a sua casa (quarto, sala, '
    #                                              'cozinha, banheiro, área, garagem, sacada, despensa)')
    #
    # TOTAL_KM_CHOICES=[
    #     (1, '5 km (até)'),
    #     (2, '6 a 10 km'),
    #     (3, '11 a 25 km'),
    #     (4, '26 km (acima de)')
    # ]
    # total_km_casa_campus = forms.ChoiceField(choices=TOTAL_KM_CHOICES, widget=forms.RadioSelect,
    #                                          label='Quantos kilômetros tem entre a sua casa e o Câmpus')
    #
    # INSTITUICAO_ANTERIOR_CHOICES = [
    #     (1, 'Particular'),
    #     (2, 'Bolsa total (mérito)'),
    #     (3, 'Bolsa parcial (mérito)'),
    #     (4, 'Bolsa parcial (vulnerabilidade)'),
    #     (5, 'Bolsa total (vulnerabilidade)'),
    #     (6, 'Pública')
    # ]
    #
    # instituicao_anterior = forms.ChoiceField(choices=INSTITUICAO_ANTERIOR_CHOICES, widget=forms.RadioSelect,
    #                                          label='Estudou anteriormente em instituição')
    #
    # VOCE_FAMILIA_CHOICES = [
    #     (1, 'Você'),
    #     (1, 'Família'),
    #     (1, 'Ambos'),
    #     (0, 'Não se aplica')
    # ]
    #
    # SAUDE = ['Faz uso, abuso de bebida alcóolica e/ou drogas?', 'Possui doença grave', 'Possui doença crônica?',
    #          'Faz uso de medicamento diário, de impacto na renda familiar'
    # ]
    #
    # saude_bebida_drogas = forms.ChoiceField(choices=VOCE_FAMILIA_CHOICES,
    #                                         widget=forms.RadioSelect(attrs={'display': 'inline-block'}),
    #                                         label=SAUDE[0])
    #
    # saude_doenca_grave = forms.ChoiceField(choices=VOCE_FAMILIA_CHOICES,
    #                                         widget=forms.RadioSelect(attrs={'display': 'inline-block'}),
    #                                         label=SAUDE[1])
    #
    # saude_doenca_cronica = forms.ChoiceField(choices=VOCE_FAMILIA_CHOICES,
    #                                        widget=forms.RadioSelect(attrs={'display': 'inline-block'}),
    #                                        label=SAUDE[2])
    #
    # saude_medicamento_diario = forms.ChoiceField(choices=VOCE_FAMILIA_CHOICES,
    #                                          widget=forms.RadioSelect(attrs={'display': 'inline-block'}),
    #                                          label=SAUDE[3])
    # PNE = [
    #     'Tem deficiência parcial de visão/audição?',
    #     'Possui deficiência física?',
    #     'Tem deficiência total  de visão/audição?',
    #     'Tem deficiência mental leve?',
    #     'Tem deficiência mental grave?',
    # ]
    #
    # PSICO = [
    #     'Sente dificuldade em se concentrar?',
    #     'Vivencia algum problema/conflito familiar',
    #     'Sofre de depressão?',
    # ]
    #
    # pne_parcial_visao_audicao = forms.ChoiceField(choices=VOCE_FAMILIA_CHOICES,
    #                                          widget=forms.RadioSelect(attrs={'display': 'inline-block'}),
    #                                          label=PNE[0])
    #
    # pne_def_fisica = forms.ChoiceField(choices=VOCE_FAMILIA_CHOICES,
    #                                          widget=forms.RadioSelect(attrs={'display': 'inline-block'}),
    #                                          label=PNE[1])
    # pne_total_visao_audicao = forms.ChoiceField(choices=VOCE_FAMILIA_CHOICES,
    #                                          widget=forms.RadioSelect(attrs={'display': 'inline-block'}),
    #                                          label=PNE[2])
    # pne_def_mental_leve = forms.ChoiceField(choices=VOCE_FAMILIA_CHOICES,
    #                                          widget=forms.RadioSelect(attrs={'display': 'inline-block'}),
    #                                          label=PNE[3])
    # pne_def_mental_grave = forms.ChoiceField(choices=VOCE_FAMILIA_CHOICES,
    #                                          widget=forms.RadioSelect(attrs={'display': 'inline-block'}),
    #                                          label=PNE[4])
    # psico_dificudade_concentrar = forms.ChoiceField(choices=VOCE_FAMILIA_CHOICES,
    #                                          widget=forms.RadioSelect(attrs={'display': 'inline-block'}),
    #                                          label=PSICO[0])
    # psico_conflito_familiar = forms.ChoiceField(choices=VOCE_FAMILIA_CHOICES,
    #                                          widget=forms.RadioSelect(attrs={'display': 'inline-block'}),
    #                                          label=PSICO[1])
    # psico_depressao = forms.ChoiceField(choices=VOCE_FAMILIA_CHOICES,
    #                                          widget=forms.RadioSelect(attrs={'display': 'inline-block'}),
    #                                          label=PSICO[2])
    #
    # ## Cultural
    #
    # COR_RACA_CHOICES = [
    #     (1, 'Branca'),
    #     (2, 'Amarela'),
    #     (3, 'Parda'),
    #     (4, 'Estrangeiro'),
    #     (5, 'Preta'),
    #     (6, 'Afro descendente Quilombola'),
    #     (7, 'Indígena'),
    #     (8, 'Estrangeiro refugiado')
    # ]
    #
    # cor_raca = forms.ChoiceField(choices=COR_RACA_CHOICES,
    #                                          widget=forms.RadioSelect,
    #                                          label='Você se considera')
    #
    # VIOLENCIA =[
    #     'Verbal(xingamentos, desacatos, etc.)',
    #     'Violência urbana(assalto, transito, etc)',
    #     'Patrimonial/financeira',
    #     'Cyberbulling (por meio de redes sociais)',
    #     'Religiosa',
    #     'Assédio Moral',
    #     'Negligência / abandono familiar',
    #     'Abuso por parte de familiares ou pessoas conhecidas',
    #     'Atentado ao pudor',
    #     'Tráfico de seres humanos',
    #     'Psicológica / moral',
    #     'Física',
    #     'Sexual'
    # ]
    #
    # violencia_verbal = forms.ChoiceField(choices=VOCE_FAMILIA_CHOICES,
    #                                          widget=forms.RadioSelect(attrs={'display': 'inline-block'}),
    #                                          label=VIOLENCIA[0])
    # violencia_urbana = forms.ChoiceField(choices=VOCE_FAMILIA_CHOICES,
    #                                          widget=forms.RadioSelect(attrs={'display': 'inline-block'}),
    #                                          label=VIOLENCIA[1])
    # violencia_patrimonial = forms.ChoiceField(choices=VOCE_FAMILIA_CHOICES,
    #                                          widget=forms.RadioSelect(attrs={'display': 'inline-block'}),
    #                                          label=VIOLENCIA[2])
    # violencia_cyberbulling = forms.ChoiceField(choices=VOCE_FAMILIA_CHOICES,
    #                                          widget=forms.RadioSelect(attrs={'display': 'inline-block'}),
    #                                          label=VIOLENCIA[3])
    # violencia_religiosa = forms.ChoiceField(choices=VOCE_FAMILIA_CHOICES,
    #                                          widget=forms.RadioSelect(attrs={'display': 'inline-block'}),
    #                                          label=VIOLENCIA[4])
    # violencia_assedio_moral = forms.ChoiceField(choices=VOCE_FAMILIA_CHOICES,
    #                                          widget=forms.RadioSelect(attrs={'display': 'inline-block'}),
    #                                          label=VIOLENCIA[5])
    # violencia_abandono = forms.ChoiceField(choices=VOCE_FAMILIA_CHOICES,
    #                                          widget=forms.RadioSelect(attrs={'display': 'inline-block'}),
    #                                          label=VIOLENCIA[6])
    # violencia_abuso_familiar = forms.ChoiceField(choices=VOCE_FAMILIA_CHOICES,
    #                                          widget=forms.RadioSelect(attrs={'display': 'inline-block'}),
    #                                          label=VIOLENCIA[7])
    # violencia_atentado_pudor = forms.ChoiceField(choices=VOCE_FAMILIA_CHOICES,
    #                                          widget=forms.RadioSelect(attrs={'display': 'inline-block'}),
    #                                          label=VIOLENCIA[8])
    # violencia_trafico_humano = forms.ChoiceField(choices=VOCE_FAMILIA_CHOICES,
    #                                          widget=forms.RadioSelect(attrs={'display': 'inline-block'}),
    #                                          label=VIOLENCIA[9])
    # violencia_psicologica_moral = forms.ChoiceField(choices=VOCE_FAMILIA_CHOICES,
    #                                          widget=forms.RadioSelect(attrs={'display': 'inline-block'}),
    #                                          label=VIOLENCIA[10])
    # violencia_fisica = forms.ChoiceField(choices=VOCE_FAMILIA_CHOICES,
    #                                          widget=forms.RadioSelect(attrs={'display': 'inline-block'}),
    #                                          label=VIOLENCIA[11])
    # violencia_sexual = forms.ChoiceField(choices=VOCE_FAMILIA_CHOICES,
    #                                          widget=forms.RadioSelect(attrs={'display': 'inline-block'}),
    #                                          label=VIOLENCIA[12])
    #
    # PRECONCEITO = [
    #     'Cultural',
    #     'Estético',
    #     'Econômico',
    #     'Religioso',
    #     'Mental',
    #     'Racial',
    #     'Gênero',
    #     'Orientação sexual'
    # ]
    #
    # preconceito_cultural = forms.ChoiceField(choices=VOCE_FAMILIA_CHOICES,
    #                                          widget=forms.RadioSelect(attrs={'display': 'inline-block'}),
    #                                          label=PRECONCEITO[0])
    # preconceito_estetico = forms.ChoiceField(choices=VOCE_FAMILIA_CHOICES,
    #                                          widget=forms.RadioSelect(attrs={'display': 'inline-block'}),
    #                                          label=PRECONCEITO[1])
    # preconceito_economico = forms.ChoiceField(choices=VOCE_FAMILIA_CHOICES,
    #                                          widget=forms.RadioSelect(attrs={'display': 'inline-block'}),
    #                                          label=PRECONCEITO[2])
    # preconceito_religioso = forms.ChoiceField(choices=VOCE_FAMILIA_CHOICES,
    #                                          widget=forms.RadioSelect(attrs={'display': 'inline-block'}),
    #                                          label=PRECONCEITO[3])
    # preconceito_mental = forms.ChoiceField(choices=VOCE_FAMILIA_CHOICES,
    #                                          widget=forms.RadioSelect(attrs={'display': 'inline-block'}),
    #                                          label=PRECONCEITO[4])
    # preconceito_racial = forms.ChoiceField(choices=VOCE_FAMILIA_CHOICES,
    #                                          widget=forms.RadioSelect(attrs={'display': 'inline-block'}),
    #                                          label=PRECONCEITO[5])
    # preconceito_genero = forms.ChoiceField(choices=VOCE_FAMILIA_CHOICES,
    #                                          widget=forms.RadioSelect(attrs={'display': 'inline-block'}),
    #                                          label=PRECONCEITO[6])
    # preconceito_orientacao_sexual  = forms.ChoiceField(choices=VOCE_FAMILIA_CHOICES,
    #                                          widget=forms.RadioSelect(attrs={'display': 'inline-block'}),
    #                                          label=PRECONCEITO[7])
    #
    # SERVICOS_INDISPONIVEIS_CHOICES = [
    #     (1, 'Táxi'),
    #     (2, 'Moto táxi'),
    #     (3, 'Transporte escolar pago'),
    #     (4, 'Ônibus escolar'),
    #     (5, 'Transporte escolar público'),
    #     (6, 'Ônibus coletivo')
    # ]
    #
    # servicos_indisponiveis_bairro = forms.ChoiceField(choices=SERVICOS_INDISPONIVEIS_CHOICES, widget=forms.CheckboxSelectMultiple,
    #                                            label='Quais são os serviços indisponiveis em seu bairro?')
    #
    # DESCARTE_LIXO_CHOICE = [
    #     (1, 'Serviço público de limpeza'),
    #     (3, 'Jogado em terreno baldio ou em via pública'),
    #     (2, 'Enterrado'),
    #     (4, 'Queimado')
    # ]
    #
    # forma_descarte_lixo = forms.ChoiceField(choices=DESCARTE_LIXO_CHOICE, widget=forms.RadioSelect,
    #                                         label='A forma de descarte do lixo de sua casa é')
    #
    # PERCEPCAO_CHOICES = [
    #     (1, 'Não oferece risco de segurança aos seus moradores'),
    #     (4, 'É considerado perigoso e os moradores sofrem  com a criminalidade'),
    #     (2, 'Os moradores se sentem seguros (há policiamento nas ruas)'),
    #     (5, 'Frequentemente os moradores sofrem  algum tipo de violência no bairro ou nos arredores'),
    #     (3, 'Não há registro de violência sofrida pelo moradores do bairro')
    # ]
    #
    # percepcao_seguranca_bairro = forms.ChoiceField(choices=PERCEPCAO_CHOICES, widget=forms.RadioSelect,
    #                                                label='Como você e/ou a sua família se sente em relação a segurança'
    #                                                      ' do seu bairro?')
    #
    # PROBLEMAS_BAIRRO_CHOICES=[
    #     (1, 'Abastecimento de água'),
    #     (1, 'Alagamentos'),
    #     (1,'Pavimentação (asfalto nas ruas)'),
    #     (1,'Energia e iluminação pública'),
    #     (1,'Ruas esburacadas (erosão)'),
    #     (1,'Saneamento básico (esgoto)'),
    #     (1,'Serviços de segurança'),
    #     (1,'Acessibilidade '),
    #     (1,'Áreas de recreaçao e lazer'),
    #     (1,'Limpeza e coleta de lixo'),
    #     (1,'Serviços de saúde'),
    #     (1,'Transporte público'),
    # ]
    #
    # problemas_bairro = forms.ChoiceField(choices=PROBLEMAS_BAIRRO_CHOICES, widget=forms.CheckboxSelectMultiple,
    #                                      label='Qual(is) o maior(es) problemas do seu bairro?')
    #
    # fale_mais_familia = forms.CharField(widget=forms.Textarea,
    #                                     label='Fale mais sobre você e a sua família.')

    title = 'Formulário Socioeconômico-Cultural'
    objetivo = 'teste'

    layout = Layout(
        Fieldset("Dados Pessoais"),
        Row(Span8('nome'),Span4('email')),
            #Span4('sexo')),
        Row(Span4('cpf'), Span8('cidade')),
            # Span4('bairro')),

        # Fieldset("Dimensão: Econômica"),
        #
        # Fieldset("Incluindo você, quantas "
        #              "pessoas moram em sua casa?"),
        # Row('dependentes_RBD'),
        #
        # Fieldset("Dessas pessoas, quantas possuem renda (seja por trabalho formal, informal, aposentadoria,etc.)?"),
        # Row('origem_renda'),
        #
        # Fieldset("Qual é o valor Renda Bruta Domiciliar (considere a renda total dos membros do domicilio "
        #          "sem os descontos)?"),
        # Row('renda_bruta_domiciliar'),
        #
        # Fieldset("Quem é o principal responsável pela manutenção do domicílio? Qual é o vinculo de parentesco?"),
        # Row('responsavel_domicilio'),
        #
        # Fieldset("Renda per capita"),
        # Row(Span4('renda_per_capita')),
        #
        # Fieldset("Dependência Financeira"),Row('relacao_financeira'),
        #
        # Fieldset("Despesas e Gastos: Saúde"),
        # Row(Column('despesas_saude_tratamento',
        #            'despesas_saude_medicamento'),
        #     Column('despesas_saude_cuidador',
        #            'despesas_saude_plano')),
        #
        # Fieldset("Despesas e Gastos: Transporte e Moradia"),
        #
        # Row(Column('despesas_transporte'),
        #     Column('despesas_moradia')),
        #
        # Fieldset("Despesas e Gastos: Educação"),
        # Row('despesas_educacao_superior'),
        # Row('despesas_educacao_basico'),
        # Row('despesas_educacao_cursinho'),
        # Row('despesas_educacao_capacitacao'),
        # Row('despesas_educacao_material'),
        #
        # Fieldset("Despesas e Gastos: Bens e Domésticas"),
        # Row(Column('despesas_bens_fcarro',
        #            'despesas_bens_fmoto',
        #            'despesas_bens_terreno'),
        #     Column('despesas_domesticas_eletrica',
        #            'despesas_domesticas_agua',
        #            'despesas_domesticas_alimentacao')),
        #
        # Fieldset("Dimensão: Social"),
        #
        # Fieldset("Manutenção do lar"),
        # Row('condicao_responsavel_casa'),
        #
        # Fieldset("Acesso ao Campus"),
        # Row('meio_acesso_campus'),
        #
        # Fieldset("Moradia"),
        # Row(Span6('condicao_moradia'),Span6('local_moradia')),
        #
        # Fieldset("Sobre sua casa"),
        # Row(Span4('total_pessoas_casa'), Span4('total_comodos_casa'),
        #     Span4('total_km_casa_campus')),
        #
        # Fieldset("Sobre sua formação anterior"),
        # Row('instituicao_anterior'),
        #
        # Fieldset("Saúde Física"),
        # Row('saude_bebida_drogas'),
        # Row('saude_doenca_grave'),
        # Row('saude_doenca_cronica'),
        # Row('saude_medicamento_diario'),
        #
        # Fieldset("Necessidades Específicas"),
        # Row('pne_parcial_visao_audicao'),
        # Row('pne_def_fisica'),
        # Row('pne_total_visao_audicao'),
        # Row('pne_def_mental_leve'),
        # Row('pne_def_mental_grave'),
        #
        # Fieldset("Saúde Psíquica"),
        # Row('psico_dificudade_concentrar'),
        # Row('psico_conflito_familiar'),
        # Row('psico_depressao'),
        #
        # Fieldset("Dimensão: Cultural"),
        #
        # Row('cor_raca'),
        #
        # Fieldset("Sofreu/sofre algum tipo de violência: "),
        # Row('violencia_verbal'),
        # Row('violencia_urbana'),
        # Row('violencia_patrimonial'),
        # Row('violencia_cyberbulling'),
        # Row('violencia_religiosa'),
        # Row('violencia_assedio_moral'),
        # Row('violencia_abandono'),
        # Row('violencia_abuso_familiar'),
        # Row('violencia_atentado_pudor'),
        # Row('violencia_trafico_humano'),
        # Row('violencia_psicologica_moral'),
        # Row('violencia_fisica'),
        # Row('violencia_sexual'),
        #
        # Fieldset("Sofreu/sofre algum tipo de preconceito: "),
        # Row('preconceito_cultural'),
        # Row('preconceito_estetico'),
        # Row('preconceito_economico'),
        # Row('preconceito_religioso'),
        # Row('preconceito_mental'),
        # Row('preconceito_racial'),
        # Row('preconceito_genero'),
        # Row('preconceito_orientacao_sexual'),
        #
        # Fieldset("Dimensão: Cultural"),
        #
        # Fieldset("Sobre seu bairro"),
        # Row(Column('servicos_indisponiveis_bairro'),
        #     Column('forma_descarte_lixo')),
        #
        # Row('percepcao_seguranca_bairro'),
        #
        # Row('problemas_bairro'),
        #
        # Fieldset("Comentários finais"),
        # Row('fale_mais_familia')


    )