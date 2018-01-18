from django import forms

class QuestionarioForm(forms.Form):
    # Dados Pessoais
    nome = forms.CharField(label='Nome')
    cpf = forms.CharField(label='CPF')

    SEXO_CHOICE = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]
    sexo = forms.ChoiceField(choices=SEXO_CHOICE, widget=forms.RadioSelect, label='Sexo')

    # Dimensão: Economica
    dependentes_RBD = forms.CharField(label='Quantidade de dependentes da Renda Bruta Domiciliar (RBD)')
    origem_renda = forms.CharField(label='Origem da renda')
    renda_bruta_domiciliar = forms.CharField(label='Renda Bruta Domiciliar')
    responsavel_domicilio = forms.CharField(label="Responsável pela manutenção do domicílio")

    # Finanças
    RENDA_PER_CAPITA_CHOICE = [
        (1, '1.405,51 (a partir)'),
        (2, '937,01 a 1405,50'),
        (3, '468,50 a 937,00'),
        (4, '234,25 até 468,49'),
        (5, 'de 0 até 234, 24')
    ]
    renda_per_capita = forms.ChoiceField(choices=RENDA_PER_CAPITA_CHOICE, widget=forms.RadioSelect,
                                         label='Renda per capita domiciliar')

    DEPENDENCIA_FINANCEIRA_CHOICE = [
        (1, 'É independente financeiramente'),
        (2, 'É independente financeiramente e responsável por parte das despesas domésticas'),
        (3, 'É independente totalmente e responsável por todas as despesas domésticas'),
        (4, 'Dependente inteiramente da renda dos pais ou companheiro(s)'),
        (5, 'Dependente inteiramente da renda de outros parentes')
    ]
    relacao_financeira = forms.ChoiceField(choices=DEPENDENCIA_FINANCEIRA_CHOICE, widget=forms.RadioSelect,
                                           label='Qual é a sua relação financeira?')

    # Despesas

    despesas_saude_tratamento = forms.CharField(label='Tratamento de saúde (a partir de R$ 234,24)')
    despesas_saude_medicamento = forms.CharField(label='Medicamentos (a partir de R$ 200,00)')
    despesas_saude_cuidador = forms.CharField(label='Cuidador de idoso/criança/PNE')
    despesas_saude_plano = forms.CharField(label='Plano de Saúde')

    despesas_transporte = forms.CharField(label='Transporte para acessar o Campus')

    despesas_moradia = forms.CharField(label='Aluguel/Financiamento')

    despesas_educacao_superior = forms.CharField(label='Educação Superior')
    despesas_educacao_basico = forms.CharField(label='Educação Básica (Fundamental e Médio')
    despesas_educacao_cursinho = forms.CharField(label='Curso Preparatório (cursinhos, etc)')
    despesas_educacao_capacitacao = forms.CharField(label='Curso de Capacitação')
    despesas_educacao_material = forms.CharField(label='Material Didático')

    despesas_bens_fcarro = forms.CharField(label='Financiamento de carro (até R$ 800,00/mês)')
    despesas_bens_fmoto = forms.CharField(label='Financiamento de moto (até R$ 300,00/mês')
    despesas_bens_terreno = forms.CharField(label='Terreno/Lote (até R$ 600,00/mês')

    despesas_domesticas_eletrica = forms.CharField(label='Energia (até R$ 200,00/mês)')
    despesas_domesticas_agua = forms.CharField(label='Água (até R$ 150,00/mês')
    despesas_domesticas_alimentacao = forms.CharField(label='Alimentação (até R$ 650,00/mês')