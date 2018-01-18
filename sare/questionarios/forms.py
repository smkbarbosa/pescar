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

    #Área Economica
    dependentes_RBD = forms.CharField(label='Quantidade de dependentes da Renda Bruta Domiciliar (RBD)')
    origem_renda = forms.CharField(label='Origem da renda')
    renda_bruta_domiciliar = forms.CharField(label='Renda Bruta Domiciliar')