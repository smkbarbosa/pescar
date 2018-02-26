from django.shortcuts import render

from sare.questionarios.forms import BuscaForm


def home(request):
    return render(request, 'index.html')


def busca(request):
    form = BuscaForm(request.POST)

    if not form.is_valid():
        return render(request, 'consulta.html',
                      {'form': form})
    return render(request, 'consulta.html', {'form':form})