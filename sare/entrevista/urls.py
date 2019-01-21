# -*- coding: utf-8 -*-
from django.conf.urls import url

from sare.entrevista.views import AlunoAutoComplete, get_aluno_information

app_name = 'entrevistas'

urlpatterns = [
    url(r'^aluno-autocomplete/$', AlunoAutoComplete.as_view(), name='aluno-autocomplete'),
    url(r'^get-aluno/$', get_aluno_information, name='get-aluno-information'),
]
