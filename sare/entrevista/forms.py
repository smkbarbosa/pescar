# -*- coding: utf-8 -*-
from django import forms
from sare.core.models import Aluno
from sare.entrevista.models import Entrevista
from dal import autocomplete


class EntrevistaForm(forms.ModelForm):
    number_choices = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5)
    )
    aluno = forms.ModelChoiceField(queryset=Aluno.objects.all(), widget=autocomplete.ModelSelect2(url='entrevista:aluno-autocomplete', attrs={'data-html':True}))
    #   Situações Problemas (SP)

    sp_1 = forms.ChoiceField(label='Dependente financeiro e sofre algum tipo de violência do responsável pelo seu sustento', widget=forms.RadioSelect(attrs={'class':'inline', }), choices=number_choices)
    sp_2 = forms.ChoiceField(label='Veio de outra localidade com objetivo de estudar no IFTO', widget=forms.RadioSelect(attrs={'class':'inline', }), choices=number_choices)
    sp_3 = forms.ChoiceField(label='Utiliza transporte intermunicipal ou rural para acessar o Campus', widget=forms.RadioSelect(attrs={'class':'inline', }), choices=number_choices)
    sp_4 = forms.ChoiceField(label='Ser estudante em tempo integral', widget=forms.RadioSelect(attrs={'class':'inline', }), choices=number_choices)
    sp_5 = forms.ChoiceField(label='Residir distante do Campus', widget=forms.RadioSelect(attrs={'class':'inline', }), choices=number_choices)
    sp_6 = forms.ChoiceField(label='Necessita fazer refeições diárias no Campus', widget=forms.RadioSelect(attrs={'class':'inline', }), choices=number_choices)
    sp_7 = forms.ChoiceField(label='Possui filhos entre 0 e 12 anos que estudam em instituições privadas', widget=forms.RadioSelect(attrs={'class':'inline', }), choices=number_choices)
    sp_8 = forms.ChoiceField(label='Necessidade de pagar cuidador (idoso/criança) por não possuir nenhum responsável durante o período que está estudando no Campus', widget=forms.RadioSelect(attrs={'class':'inline', }), choices=number_choices)
    sp_9 = forms.ChoiceField(label='Morar com o(s) filho(s) no mesmo ambiente familiar', widget=forms.RadioSelect(attrs={'class':'inline', }), choices=number_choices)
    sp_10 = forms.ChoiceField(label='Desenvolver ou praticar qualquer modadilidade esportiva no Campus com acompanhamento do Professor', widget=forms.RadioSelect(attrs={'class':'inline', }), choices=number_choices)
    sp_11 = forms.ChoiceField(label='Frequentar curso que esija material de uso pessoal e que seja específico do curso', widget=forms.RadioSelect(attrs={'class':'inline', }), choices=number_choices)
    sp_12 = forms.ChoiceField(label='Ter carga horária disponível que não afete o desenvolvimento escolar',widget=forms.RadioSelect(attrs={'class':'inline', }), choices=number_choices)
    sp_13 = forms.ChoiceField(label='Estudante vai ao Campus mais de 3 dias na semana para cursar disciplinas', widget=forms.RadioSelect(attrs={'class':'inline', }), choices=number_choices)
    sp_14 = forms.ChoiceField(label='Aluno sai do trabalho e vai direto para o Campus', widget=forms.RadioSelect(attrs={'class':'inline', }), choices=number_choices)
    sp_15 = forms.ChoiceField(label='Situação de doença crônica ou grave impacto na renda familiar', widget=forms.RadioSelect(attrs={'class':'inline', }), choices=number_choices)
    sp_16 = forms.ChoiceField(label='Não tem com quem deixar o(s) filho(s) para estudar', widget=forms.RadioSelect(attrs={'class':'inline', }), choices=number_choices)

    #   Finalização da Entrevista (FN)
    fn_1 = forms.ChoiceField(label='Condição de renda oriunda da informalidade', widget=forms.RadioSelect(attrs={'class':'inline', }), choices=number_choices)
    fn_2 = forms.ChoiceField(label='Adulto ou chefe de família com baixa escolaridade', widget=forms.RadioSelect(attrs={'class':'inline', }), choices=number_choices)
    fn_3 = forms.ChoiceField(label='Dependência de renda de idoso', widget=forms.RadioSelect(attrs={'class':'inline', }), choices=number_choices)
    fn_4 = forms.ChoiceField(label='Domicílio em precário estado de construção apresentando sinais de fragilidades na estrutura', widget=forms.RadioSelect(attrs={'class':'inline', }), choices=number_choices)
    fn_5 = forms.ChoiceField(label='Condição de renda oriunda da informalidade', widget=forms.RadioSelect(attrs={'class':'inline', }), choices=number_choices)
    fn_6 = forms.ChoiceField(label='Aluno com problemas graves indentificadas durante a entrevista', widget=forms.RadioSelect(attrs={'class': 'inline', }), choices=number_choices)


    class Meta:
        model = Entrevista
        fields = '__all__'

