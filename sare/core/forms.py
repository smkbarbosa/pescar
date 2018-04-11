from django import forms
from django.forms import Select, RadioSelect
from material import *


from sare.core.models import Aluno, Endereco


class AlunoForm(forms.ModelForm):

    title = 'Formulário Socioeconômico-Cultural'

    layout = Layout(
        Fieldset("Dados Pessoais"),
        Row(Span4('nome'), Span4('email'),
            Span2('cpf'), Span2('fone')),
        Row(Span4('sexo')),

        Fieldset('Dados acadêmicos'),
        Field('curso'),
        Row(Span4('sem_mod_ano'), Span4('matricula'), Span4('campus')))

    class Meta:
        model = Aluno
        fields = '__all__'
        widgets = {
            'curso': Select,
            'sexo': RadioSelect
        }

        help_texts = {
            'cpf': 'Somente números',
        }


class EnderecoForm(forms.ModelForm):

    layout = Layout(
        Fieldset('Endereço:'),
        Row(Span3('cep'),
            Span5('endereco')),
        Row(Span3('num_casa'), Span3('bairro'), Span3('cidade'), Span3('estado')
            )
    )

    class Meta:
        model = Endereco
        fields = '__all__'

