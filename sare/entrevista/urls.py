# -*- coding: utf-8 -*-
from django.conf.urls import url

from sare.entrevista.views import AlunoAutoComplete


urlpatterns = [
    url(r'^aluno-autocomplete/$', AlunoAutoComplete.as_view(), name='aluno-autocomplete'),
]
