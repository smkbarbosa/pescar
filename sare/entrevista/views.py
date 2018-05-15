# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from dal import autocomplete
from sare.core.models import Aluno
from django.urls import reverse

from django.db.models import Q
# Create your views here.


class AlunoAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Aluno.objects.none()
        qs = Aluno.objects.all()
        if self.q:
            qs = qs.filter(Q(nome__icontains=self.q)|Q(cpf__icontains=self.q))
        return qs
    def get_results(self, context):
        return [
            {
                'id': self.get_result_value(result),
                'text': self.get_result_label(result),
                'nome':self.get_name(result),
                'cpf': self.get_cpf(result),
            }
            for result in context['object_list']
        ]
    def get_name(self, result):
        return result.nome

    def get_cpf(self, result):
        return result.cpf
