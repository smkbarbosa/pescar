from django.shortcuts import render

from sare.questionarios.forms import BuscaForm


def home(request):
    return render(request, 'index.html')


def busca(request):
    form = BuscaForm()

    return render(request, 'consulta.html', {'form':form})