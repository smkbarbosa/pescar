# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from dal import autocomplete
from sare.core.models import Aluno
from django.urls import reverse
from django.utils.html import format_html


from django.http import JsonResponse
import json
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

    # def get_selected_result_label(self, item):
    #     return item.nome
    
    # def get_result_label(self, item):
    #     return item.nome


    def get_result_label(self, item):
        return format_html('<b>Nome:</b>{} <b>CPF</b>:{}', item.nome, item.cpf)

    # def get_selected_result_label(self, item):
    #     return item.nome





def get_aluno_information(request):
    id=request.GET['id']

    # import ipdb; 
    # ipdb.set_trace()
    if id:
        try:
            aluno = Aluno.objects.get(id=id)
            aluno_dict = {
                'nome': aluno.nome,
                'cpf': aluno.cpf,
                'email': aluno.email,
                'telefone': aluno.fone,
                'matricula': aluno.matricula
            }
            # dump = json.dumps(aluno_dict)
            return JsonResponse(aluno_dict)
        except Exception as inst:
            error={'error':'erro'}
            return JsonResponse(error)
    else:
        error={'error':'erro'}
        return JsonResponse(error) 

